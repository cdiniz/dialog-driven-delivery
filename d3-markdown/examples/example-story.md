---
type: story
id: story-2
spec: specs/user-authentication.md
title: User Login
status: done
priority: high
size: medium
estimate: 3 days
actual: 3 days
created: 2026-01-27
started: 2026-01-28
completed: 2026-01-30
dependencies: [story-1]
blocks: [story-5]
labels: [authentication, backend, frontend, api]
---

# Story: User Login

**As a** registered user
**I want** to log in with my email and password
**So that** I can access my account and personalized content

**Value:** Users can authenticate and access their dashboard with personalized content

**Specification:** [User Authentication](../../specs/user-authentication.md)

---

## Acceptance Criteria

**AC1: Successful login with valid credentials**
- **Given** a registered and verified user with email "user@example.com"
- **When** they enter their email and correct password and click "Log In"
- **Then** they are redirected to "/dashboard"
- **And** a secure session cookie is set with 24-hour expiration
- **And** their user information is displayed in the dashboard

**AC2: Failed login with wrong password**
- **Given** a registered user with email "user@example.com"
- **When** they enter their email but an incorrect password
- **And** click "Log In"
- **Then** they see an error message "Invalid email or password"
- **And** they remain on the login page
- **And** the failed attempt is logged
- **And** the login form is cleared

**AC3: Account lockout after failed attempts**
- **Given** a user has failed to login 4 times in the last 15 minutes
- **When** they attempt to login a 5th time (even with correct credentials)
- **Then** they see an error "Account locked for 30 minutes due to too many failed attempts"
- **And** they cannot login until the lockout period expires
- **And** they receive an email notification about the lockout

**AC4: Login with unverified account**
- **Given** a user registered but has not verified their email
- **When** they attempt to login with correct credentials
- **Then** they see an error "Please verify your email address"
- **And** they see a "Resend Verification" button
- **And** they remain on the login page

**AC5: "Remember me" functionality**
- **Given** a user with valid credentials
- **When** they check the "Remember me" checkbox and login
- **Then** their session is set to expire in 30 days instead of 24 hours
- **And** they remain logged in when closing and reopening the browser

**AC6: Rate limiting protection**
- **Given** an IP address has made 5 login attempts in the last 15 minutes
- **When** they attempt a 6th login from the same IP
- **Then** they receive a 429 "Too Many Requests" response
- **And** they see "Too many login attempts. Please try again in 15 minutes"
- **And** the rate limit resets after 15 minutes

**AC7: Concurrent sessions allowed**
- **Given** a user is logged in on Device A
- **When** they log in on Device B with the same credentials
- **Then** both sessions remain active
- **And** they can use the application on both devices
- **And** each session has its own expiration

---

## Technical Notes

### Backend Implementation

**Endpoint:** `POST /api/auth/login`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecureP@ss123",
  "rememberMe": false
}
```

**Response (200):**
```json
{
  "success": true,
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "verified": true
  },
  "token": "jwt-token"
}
```

**Implementation Steps:**
1. Validate request body (email format, password present)
2. Check rate limit in Redis (key: `rate_limit:login:{ip}`)
3. Query user from PostgreSQL by email
4. Check if account is locked (`account_locked_until` field)
5. Verify password using `bcrypt.compare()`
6. If password invalid:
   - Increment `failed_login_attempts`
   - If attempts >= 5, set `account_locked_until` = now + 30 minutes
   - Return 401 error
7. If password valid:
   - Reset `failed_login_attempts` to 0
   - Generate JWT token with user data
   - Store session in Redis with appropriate TTL
   - Set secure HTTP-only cookie
   - Return user data and token

**Security:**
- bcrypt cost factor: 12 (~200ms verification time)
- JWT secret from environment variable
- Secure cookie flags: `httpOnly`, `secure`, `sameSite: strict`
- Rate limiting: 5 attempts per 15 minutes per IP

### Frontend Implementation

**Component:** `LoginForm.jsx`

**State Management:**
```javascript
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [rememberMe, setRememberMe] = useState(false);
const [error, setError] = useState('');
const [loading, setLoading] = useState(false);
```

**Validation:**
- Email: Validate format on blur
- Password: Validate presence on blur
- Show inline errors below fields

**Submission:**
```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  setError('');
  setLoading(true);

  try {
    const response = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, rememberMe }),
      credentials: 'include', // Include cookies
    });

    if (!response.ok) {
      const data = await response.json();
      setError(data.error.message);
      return;
    }

    // Success - redirect to dashboard
    window.location.href = '/dashboard';
  } catch (err) {
    setError('Network error. Please try again.');
  } finally {
    setLoading(false);
  }
};
```

### Database Updates

**Modified Table:** `users`

**New Fields:**
```sql
ALTER TABLE users
ADD COLUMN failed_login_attempts INTEGER DEFAULT 0,
ADD COLUMN account_locked_until TIMESTAMP NULL;

CREATE INDEX idx_users_account_locked ON users(account_locked_until);
```

### Redis Keys

**Rate Limiting:**
- Key: `rate_limit:login:{ip_address}`
- Value: attempt count (integer)
- TTL: 900 seconds (15 minutes)

**Session Storage:**
- Key: `session:{user_id}:{session_id}`
- Value: JSON object with token, created_at, expires_at
- TTL: 86400 seconds (24 hours) or 2592000 (30 days with remember me)

---

## Testing

### Unit Tests

```javascript
describe('Login Validation', () => {
  test('rejects invalid email format', () => {
    expect(validateEmail('notanemail')).toBe(false);
  });

  test('requires password', () => {
    expect(validatePassword('')).toBe(false);
  });
});

describe('Login Authentication', () => {
  test('authenticates valid credentials', async () => {
    const result = await authenticateUser('user@example.com', 'correct');
    expect(result.success).toBe(true);
  });

  test('rejects invalid password', async () => {
    const result = await authenticateUser('user@example.com', 'wrong');
    expect(result.success).toBe(false);
  });

  test('locks account after 5 failed attempts', async () => {
    for (let i = 0; i < 5; i++) {
      await authenticateUser('user@example.com', 'wrong');
    }
    const result = await authenticateUser('user@example.com', 'correct');
    expect(result.error.code).toBe('ACCOUNT_LOCKED');
  });
});
```

### Integration Tests

```javascript
describe('Login Flow', () => {
  test('full login flow with valid credentials', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'TestPass123' });

    expect(response.status).toBe(200);
    expect(response.body.success).toBe(true);
    expect(response.headers['set-cookie']).toBeDefined();
  });

  test('rate limiting after 5 attempts', async () => {
    for (let i = 0; i < 5; i++) {
      await request(app)
        .post('/api/auth/login')
        .send({ email: 'test@example.com', password: 'wrong' });
    }

    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@example.com', password: 'wrong' });

    expect(response.status).toBe(429);
  });
});
```

### Test Coverage

```bash
npm test -- --coverage

Expected coverage:
- Statements: >85%
- Branches: >80%
- Functions: >85%
- Lines: >85%
```

---

## Definition of Done

- [x] Backend endpoint implemented (`POST /api/auth/login`)
- [x] Frontend login form implemented
- [x] Password verification with bcrypt working
- [x] Rate limiting enforced (5 per 15 min)
- [x] Account lockout working (5 failed attempts → 30 min lock)
- [x] "Remember me" functionality working
- [x] Session storage in Redis working
- [x] Unit tests written and passing (12/12)
- [x] Integration tests written and passing (8/8)
- [x] Security review completed
- [x] Performance tested (<300ms average login time)
- [x] API documentation updated
- [x] Code reviewed and approved
- [x] Merged to main branch
- [x] Deployed to staging
- [x] QA testing completed
- [x] Deployed to production

---

## Implementation Notes

**Challenges Faced:**
1. bcrypt verification was taking >500ms initially → reduced cost factor from 14 to 12
2. Rate limiting was per-user initially, changed to per-IP for better security
3. Concurrent sessions required separate session IDs in Redis keys

**Decisions Made:**
1. Allow concurrent sessions (user feedback: wanted to stay logged in on phone and desktop)
2. Use IP-based rate limiting instead of user-based (prevents pre-authentication DoS)
3. Lock account on 5th attempt (not 6th) to be more security-conscious

**Performance:**
- Average login time: 250ms
- 95th percentile: 380ms
- bcrypt verification: ~200ms
- Database query: ~30ms
- Redis operations: ~10ms

---

## Dependencies

**Blocked by:**
- [x] story-1: User Registration (needed to have users to test login)

**Blocks:**
- [ ] story-5: Session Management (login creates sessions)

---

## References

- Specification: [User Authentication](../../specs/user-authentication.md)
- API Docs: `/docs/api/auth/login`
- PR: #123 (https://github.com/myorg/myrepo/pull/123)
- Deploy: Deployed to production on 2026-01-30

---

## Metrics (Post-Deployment)

**Week 1:**
- Login attempts: 1,247
- Success rate: 94.3%
- Failed attempts: 71 (5.7%)
- Account lockouts: 3 (0.24%)
- Average response time: 260ms
- 95th percentile: 390ms

**User Feedback:**
- 92% satisfaction with login experience
- 2 support tickets about account lockouts (both resolved - users forgot passwords)
- 1 request for social login (tracked for Phase 2)
