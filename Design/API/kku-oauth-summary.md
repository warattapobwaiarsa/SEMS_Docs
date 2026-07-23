# KKU OAuth 2.1 · OIDC Authentication Service

## Overview & Executive Summary

The **KKU OAuth 2.1 / OpenID Connect (OIDC) service** (`oauth.kku.ac.th`) is Khon Kaen University's centralized authentication platform. It enables third-party and internal applications to authenticate users via KKU's **Single Sign-On (SSO)** credentials using industry-standard protocols — **OAuth 2.1** for authorization and **OpenID Connect** for identity verification.

The service is standards-based, supporting **automatic endpoint discovery**, **PKCE (Proof Key for Code Exchange)** for secure authorization code flows, and **verifiable ID tokens** for identity assurance. It is designed to let developers integrate KKU login into their applications without managing credentials directly, while also maintaining a legacy endpoint for backward compatibility with older KKU integrations.

## Key Features & Capabilities

- **OAuth 2.1 Compliant** — implements the latest OAuth security best practices (mandatory PKCE, no implicit grant).
- **OpenID Connect (OIDC) Support** — issues standards-compliant `id_token`s for identity verification.
- **Discovery Endpoint** — clients can auto-configure using `.well-known/openid-configuration`.
- **PKCE Enforcement** — all authorization code exchanges require `S256` code challenge/verifier pairs.
- **Token Introspection & Revocation** — supports RFC 7662 introspection and token revocation for session management.
- **Flexible Logout** — supports both **per-application logout** and **full SSO logout**.
- **Legacy Compatibility** — retains `/api/v2/user` for existing integrations while recommending `/userinfo` for new development.
- **JWKS Support** — publishes public signing keys for token signature verification.
- **Bilingual Interface** — supports both Thai (ไทย) and English, with light/dark theme options.

## Technical Specifications / Authentication Flow

### Available Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `GET` | `/.well-known/openid-configuration` | OIDC discovery — auto-detects endpoints and signing keys |
| `GET` | `/authorize` | Initiates Authorization Code flow with PKCE (`scope=openid` for OIDC) |
| `POST` | `/token` | Exchanges authorization code or refresh token for access/ID tokens |
| `GET` | `/userinfo` | Returns standard OIDC claims (requires `Authorization: Bearer <token>`) |
| `POST` | `/introspect` | RFC 7662 token introspection (client-authenticated) |
| `POST` | `/revoke` | Revokes an active token |
| `GET` | `/.well-known/jwks.json` | Publishes JSON Web Key Set for signature verification |
| `GET` | `/api/v2/user` | Legacy KKU user endpoint (deprecated in favor of `/userinfo`) |
| `GET` | `/logout` | Per-app or full SSO logout, depending on parameters |

### Authentication Flow (Step-by-Step)

**Step 1 — Redirect User to Authorize**

```
GET /authorize?client_id={client_id}
&redirect_uri={redirect_uri}
&response_type=code
&scope=openid profile email
&state={state}
&nonce={nonce}
&code_challenge={code_challenge}
&code_challenge_method=S256
```

- `state` — CSRF protection; must be verified on callback.
- `nonce` — bound into the `id_token`; must be verified on return.
- `code_challenge` — computed as `BASE64URL(SHA256(code_verifier))`; only `S256` is supported.
- Including `scope=openid` is required to receive an `id_token`.

**Step 2 — Exchange Authorization Code for Tokens**

```
POST /token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code={authorization_code}
&redirect_uri={redirect_uri}
&code_verifier={code_verifier}
&client_id={client_id}
&client_secret={client_secret}
```

- Returns `access_token`, `refresh_token`, and (if `openid` was requested) an `id_token`.
- Client credentials may alternatively be passed via `Authorization: Basic` header.

**Step 3 — Fetch User Data**

```
GET /userinfo
Authorization: Bearer {access_token}
```

- Returns standard OIDC claims scoped to the granted consent.
- The `sub` claim matches the one in the `id_token`.
- The legacy `/api/v2/user` endpoint remains functional for existing integrations.

**Step 4 — Refresh Token (Optional)**

```
POST /token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token={refresh_token}
&client_id={client_id}
&client_secret={client_secret}
```

**Step 5 — Logout**

```
GET /logout?client_id={client_id}&redirect_uri={redirect_uri}   # Per-app logout
GET /logout?redirect_uri={redirect_uri}                          # Full SSO logout
```

- **Per-app logout**: signs the user out of the requesting application only; SSO session and other apps remain active.
- **Full logout**: terminates the user's SSO session across all connected applications.

## Usage Guidelines / Integration Instructions

1. **Register your application** to obtain a `client_id` and `client_secret` (registration process not detailed on the public page — likely handled through KKU IT administration).
2. **Use discovery** (`/.well-known/openid-configuration`) to auto-configure your OIDC client rather than hardcoding endpoints.
3. **Always implement PKCE** (`S256`) — this is mandatory, not optional, under OAuth 2.1.
4. **Verify `state` and `nonce`** values on every callback to prevent CSRF and replay attacks.
5. **Prefer `/userinfo` over `/api/v2/user`** for all new development; the legacy endpoint is maintained only for backward compatibility.
6. **Validate ID tokens** using the public keys published at `/.well-known/jwks.json`.
7. **Choose the correct logout type** depending on whether the application should end just its own session or the user's entire SSO session.

## Summary Table — Key Takeaways

| Aspect | Detail |
|---|---|
| **Protocol** | OAuth 2.1 + OpenID Connect |
| **Security Model** | PKCE-only (`S256`), no implicit grant |
| **Discovery** | Supported via `/.well-known/openid-configuration` |
| **Token Types** | `access_token`, `refresh_token`, `id_token` |
| **Identity Claims** | Retrieved via `/userinfo` (preferred) or `/api/v2/user` (legacy) |
| **Session Termination** | Configurable — per-app or full SSO logout |
| **Key Verification** | Public keys via `/.well-known/jwks.json` |
| **Token Lifecycle Management** | `/introspect` (check validity), `/revoke` (invalidate) |
| **Ideal For** | Applications requiring KKU SSO login integration |

---
*Note: This summary is based solely on the publicly documented information available on the `oauth.kku.ac.th` landing page as of the review date. Client registration procedures, rate limits, and detailed error-handling behavior are not published on this page and should be confirmed directly with KKU's IT/authentication administrators.*
