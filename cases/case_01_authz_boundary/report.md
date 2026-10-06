# Case 01 — Authorization boundary

## Finding

**Severity: High**

The function accepts the caller tenant as an input but the buggy implementation never checks it against the order owner. A caller from tenant alpha can request an order belonging to tenant beta when the object ID is known.

This is an IDOR-style authorization failure at the object boundary.

## Evidence

The proof test requests order 202 as tenant alpha and expects access to be denied. In the buggy implementation no exception is raised, so the proof test fails as expected.

## Root cause

Authorization-relevant context is present in the function signature but is treated as informational rather than enforced policy.

## Minimal fix

Compare the object's tenant_id with the caller tenant before returning the object. Deny on mismatch.

## Regression coverage

The fixed implementation is tested for both cross-tenant denial and same-tenant success.

## Review note

A repository containing a tenant_id field is not automatically tenant-safe. The relevant claim is whether the authorization boundary is enforced on every object access path.
