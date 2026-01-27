# Feature: User Authentication

**Specification:** specs/user-authentication.md

---

## 📋 Product Specification

### 1. Overview

#### What & Why
Implement a complete user authentication system that allows users to create accounts, log in securely, and manage their sessions. This is foundational for personalizing the user experience and protecting user data.

#### Target Users & Success Metrics
- **Users:** All application users (new and returning)
- **Success Metrics:**
  - 95% of new users successfully create accounts within 2 minutes
  - <5% login failure rate (excluding incorrect passwords)
  - <3% password reset requests per month
  - 90% user satisfaction with authentication process

---

### 2. User Journey

#### Primary Workflow: New User Signup
**When:** User wants to create a new account

**Steps:**
1. User clicks "Sign Up" button on homepage
2. System displays registration form (email, password, confirm password)
3. User enters email and password (8+ characters)
4. User confirms password
5. System validates inputs (email format, password strength, passwords match)
6. System creates account and sends verification email
7. User clicks verification link in email
8. System confirms account and redirects to dashboard

**Success:** User has verified account and is logged in to dashboard

**Edge Cases:**
- **Email already exists**: Show error "Email already registered. Try logging in?"
- **Weak password**: Show strength indicator and requirements in real-time
- **Verification email not received**: Provide "Resend verification" button

#### Secondary Workflow: Returning User Login
**When:** Registered user wants to access their account

**Steps:**
1. User clicks "Log In" button
2. System displays login form (email, password)
3. User enters credentials
4. System validates credentials
5. System creates session (24h expiry) and redirects to dashboard

**Success:** User is authenticated and viewing their dashboard

**Edge Cases:**
- **Wrong password**: Show error after 3 attempts, offer "Forgot Password?"
- **Account locked**: After 5 failed attempts, lock for 30 minutes
- **Unverified account**: Show "Please verify your email" with resend option

#### Tertiary Workflow: Password Reset
**When:** User forgot their password

**Steps:**
1. User clicks "Forgot Password?" on login page
2. System displays email entry form
3. User enters registered email
4. System sends password reset email (expires in 1 hour)
5. User clicks reset link in email
6. System displays new password form
7. User enters and confirms new password
8. System updates password and confirms success
9. User is prompted to log in with new password

**Success:** User can log in with new password

---

### 3. Requirements

#### Must Have (Core Features)

* **User Registration:**
  - Input: Email (valid format), password (8+ chars), password confirmation
  - Validation:
    - Email: RFC 5322 format, not already registered
    - Password: Min 8 chars, 1 uppercase, 1 lowercase, 1 number
    - Confirmation: Must match password exactly
  - Error messages:
    - "Email is invalid" (immediately on blur)
    - "Email already registered" (on submit)
    - "Password must be at least 8 characters with 1 uppercase, 1 lowercase, and 1 number"
    - "Passwords do not match"
  - Output: Account created, verification email sent

* **Email Verification:**
  - Send verification email within 5 seconds of registration
  - Verification link expires after 24 hours
  - Allow resending verification email (max 3 times per hour)
  - Account cannot access protected features until verified

* **User Login:**
  - Input: Email and password
  - Validation: Check credentials against database
  - Session: Create 24-hour session cookie (secure, httpOnly, sameSite)
  - Rate limiting: Max 5 attempts per 15 minutes per IP
  - Output: Authenticated session, redirect to dashboard

* **Password Reset:**
  - Send reset email with 1-hour expiration token
  - Reset link is single-use (invalidated after use)
  - New password must meet same requirements as registration
  - Notify user via email when password is changed

* **Session Management:**
  - Sessions expire after 24 hours of inactivity
  - "Remember me" option extends session to 30 days
  - Allow logout from all devices (invalidate all sessions)

#### Out of Scope

* Social login (OAuth via Google, GitHub) - Phase 2
* Two-factor authentication (2FA) - Phase 2
* Biometric authentication - Phase 3
* Single Sign-On (SSO) integration - Enterprise feature
* Magic links (passwordless login) - Future consideration

#### Constraints & Dependencies

* **Technical:**
  - Must use bcrypt for password hashing (cost factor: 12)
  - Email service: SendGrid (already integrated)
  - Session storage: Redis (already set up)
  - Database: PostgreSQL (existing)

* **Business:**
  - Must comply with GDPR (data retention, right to deletion)
  - Must meet OWASP authentication guidelines
  - Password policy cannot be changed without security team approval

* **Dependencies:**
  - Depends on: Email service operational, Redis available
  - Blocks: User profile management, personalization features

---

### 4. Open Questions

#### Needs Answer Before Implementation

**Q1:** Should we support login with username instead of just email?
  - Owner: Product
  - Needed by: Before design
  - Context: Affects database schema and UI

**Q2:** What should the rate limiting policy be for password reset requests?
  - Owner: Security team
  - Needed by: Before development
  - Context: Balance between UX and security

**Q3:** Should email verification be required before login, or allow login with limited access?
  - Owner: Product
  - Needed by: Before development
  - Impact: Changes user flow significantly

#### Assumptions We're Making

1. **Email Service:** We're assuming SendGrid has >99% uptime. If SendGrid is down, authentication will be degraded. Impact: Users can't register or reset passwords during outage.

2. **Single Device:** We're assuming users typically use one device. "Remember me" doesn't sync across devices. Why reasonable: Mobile app is Phase 2. Impact if wrong: User friction if they switch devices frequently.

3. **English Only:** We're assuming authentication flows are English-only. Why reasonable: i18n is planned for Q2. Impact if wrong: International users may struggle, but core functionality works.

---

## 🔧 Technical Specification

### 1. Technical Approach

**Authentication Strategy:** JWT (JSON Web Tokens) for stateless authentication with Redis for session management.

**Architecture Pattern:**
- Backend API handles all authentication logic
- Frontend is a thin client that stores JWT in secure cookie
- Redis stores session metadata for invalidation support

**Password Security:**
- Hash with bcrypt (cost factor: 12)
- Store salt with hash (bcrypt handles this automatically)
- Never log or transmit plain-text passwords

**Email Delivery:**
- SendGrid API for transactional emails
- Template-based emails (verification, password reset)
- Retry logic: 3 attempts with exponential backoff

---

### 2. Architecture

#### System Components

```
[Frontend: React]
       ↓ HTTPS
[API Gateway: Express]
       ↓
[Auth Service: Node.js]
   ↓           ↓
[PostgreSQL] [Redis]
   ↓
[SendGrid API]
```

#### Authentication Flow Diagram

```
Registration:
User → Frontend → POST /api/auth/register → Auth Service
                                           ↓
                                   Create user record
                                           ↓
                                   Hash password (bcrypt)
                                           ↓
                                   Store in PostgreSQL
                                           ↓
                                   Generate verification token
                                           ↓
                                   Send email via SendGrid
                                           ↓
                                   Return success response

Login:
User → Frontend → POST /api/auth/login → Auth Service
                                        ↓
                                  Validate credentials
                                        ↓
                                  Check rate limit (Redis)
                                        ↓
                                  Verify password (bcrypt.compare)
                                        ↓
                                  Generate JWT token
                                        ↓
                                  Store session in Redis (24h TTL)
                                        ↓
                                  Set secure cookie
                                        ↓
                                  Return user data
```

---

### 3. API Contracts

#### POST /api/auth/register

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecureP@ss123",
  "passwordConfirm": "SecureP@ss123"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Account created. Please check your email to verify.",
  "userId": "uuid-here"
}
```

**Errors:**
- `400`: Validation errors (email invalid, password weak, passwords don't match)
- `409`: Email already registered
- `500`: Server error

#### POST /api/auth/login

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecureP@ss123",
  "rememberMe": false
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "verified": true
  },
  "token": "jwt-token-here"
}
```

**Headers:** Sets secure HTTP-only cookie with JWT

**Errors:**
- `400`: Missing email or password
- `401`: Invalid credentials
- `423`: Account locked (too many failed attempts)
- `403`: Account not verified
- `429`: Too many requests (rate limited)

#### POST /api/auth/logout

**Headers:** Requires `Authorization: Bearer <token>`

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

#### POST /api/auth/forgot-password

**Request:**
```json
{
  "email": "user@example.com"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "If that email exists, we sent a reset link."
}
```

**Note:** Always returns success to prevent email enumeration

#### POST /api/auth/reset-password

**Request:**
```json
{
  "token": "reset-token-from-email",
  "password": "NewSecureP@ss123",
  "passwordConfirm": "NewSecureP@ss123"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Password reset successfully. Please log in."
}
```

**Errors:**
- `400`: Invalid or expired token
- `400`: Password validation failed

#### GET /api/auth/verify-email/:token

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Email verified successfully"
}
```

Redirects to login page after verification.

---

### 4. Data Models

#### User Table

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  verified BOOLEAN DEFAULT FALSE,
  verification_token VARCHAR(255),
  verification_expires TIMESTAMP,
  reset_token VARCHAR(255),
  reset_expires TIMESTAMP,
  failed_login_attempts INTEGER DEFAULT 0,
  account_locked_until TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_verification_token ON users(verification_token);
CREATE INDEX idx_users_reset_token ON users(reset_token);
```

#### Session Storage (Redis)

```
Key: session:{userId}
Value: {
  "token": "jwt-token",
  "createdAt": "2026-01-27T10:00:00Z",
  "expiresAt": "2026-01-28T10:00:00Z",
  "userAgent": "...",
  "ipAddress": "..."
}
TTL: 86400 seconds (24 hours)
```

#### Rate Limiting (Redis)

```
Key: rate_limit:login:{ip}
Value: attempt_count
TTL: 900 seconds (15 minutes)

Key: rate_limit:reset:{email}
Value: attempt_count
TTL: 3600 seconds (1 hour)
```

---

### 5. Security Considerations

#### Password Security
- bcrypt with cost factor 12 (192ms on modern CPU)
- Never store plain-text passwords
- Never log passwords (even hashed)
- Require strong passwords (enforced on client and server)

#### Rate Limiting
- Login: 5 attempts per 15 minutes per IP
- Password reset: 3 attempts per hour per email
- Email verification resend: 3 per hour per user

#### Session Security
- JWT tokens with 24h expiration
- Secure, HTTP-only, SameSite cookies
- Redis stores session metadata for invalidation
- Support logout from all devices

#### OWASP Top 10 Compliance
- Prevent SQL injection (use parameterized queries)
- Protect against CSRF (SameSite cookies)
- Prevent timing attacks (constant-time comparison)
- Return generic error messages (prevent email enumeration)
- Log authentication events for monitoring

---

### 6. Error Handling

#### Client-Side Validation
- Real-time email format validation
- Password strength meter
- Password match confirmation
- Display errors inline below fields

#### Server-Side Validation
- Re-validate all inputs (never trust client)
- Return specific validation errors
- Log validation failures for monitoring

#### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Password must meet complexity requirements",
    "details": {
      "field": "password",
      "requirements": ["min 8 chars", "1 uppercase", "1 lowercase", "1 number"]
    }
  }
}
```

---

### 7. Testing Strategy

#### Unit Tests
- Password hashing and comparison
- JWT token generation and validation
- Input validation functions
- Rate limiting logic

#### Integration Tests
- Registration flow end-to-end
- Login flow end-to-end
- Password reset flow end-to-end
- Email verification flow end-to-end
- Account lockout after failed attempts
- Session expiration

#### Security Tests
- SQL injection attempts
- XSS attempts in email/password fields
- CSRF protection
- Rate limit enforcement
- Password brute force protection

#### Performance Tests
- bcrypt hashing time (should be ~200ms)
- Login response time (<500ms)
- Concurrent login requests (1000/sec)

**Target Coverage:** 85% code coverage minimum

---

### 8. Monitoring & Logging

#### Metrics to Track
- Registration success rate
- Login success rate
- Failed login attempts (by IP and by user)
- Password reset requests
- Email delivery success rate
- Session creation/expiration
- Account lockouts

#### Logging
- All authentication events (login, logout, registration)
- Failed authentication attempts (with IP address)
- Password resets (initiated and completed)
- Email verification (sent and confirmed)

**Log Level:**
- INFO: Successful authentications
- WARN: Failed login attempts
- ERROR: System failures (email not sent, database errors)

**PII Handling:** Never log passwords or tokens. Hash email addresses in logs.

---

## References

- **Related Docs:**
  - OWASP Authentication Cheat Sheet
  - Company Security Policy v2.1
  - Email Service Integration Guide
