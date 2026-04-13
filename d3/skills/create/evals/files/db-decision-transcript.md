# Meeting: Database choice for the events service
**Date:** Apr 2

## Transcript

Lead: OK so we need to pick a database for the new events service. We've been bouncing between Postgres and DynamoDB for two weeks. I want to land it today.

Eng A: My main concern with DynamoDB is the access patterns. We already know we'll need to query events by user, by time range, AND by event type. That's three different access patterns and DynamoDB makes you commit to them upfront via secondary indexes. If product changes their mind in three months we're stuck rebuilding indexes.

Eng B: Yeah and our team already runs Postgres for the user service. We have the on-call playbook, the backup story, the migration tooling. Adopting DynamoDB means a whole second operational track.

Lead: What about the write volume argument? That was the original reason we even considered DynamoDB.

Eng A: I pulled the numbers. We're projecting maybe 200 writes per second at peak in year one. Postgres handles that without breaking a sweat on the instance class we already use.

Eng B: Plus we get transactions, which the billing integration is going to need.

Lead: OK. I'm convinced. Let's go with Postgres. Any objections? ... No? Great. Postgres it is.

Eng A: One thing we didn't talk about — what about the schema? Are we doing one big events table or partitioning by event type?

Lead: Good question, but let's not solve that today. Park it, we'll come back to it next week with a proposal.

Eng B: And we should figure out the retention story too. Are we keeping events forever or rolling them off after some period? That has cost implications.

Lead: Also park it. Let's get the decision recorded and circle back on schema and retention separately.
