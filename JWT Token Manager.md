# JWT Token Manager

Handles JSON Web Token creation, validation, and lifecycle management.

## Core Functionality

- Token generation with custom claims
- Token validation and verification  
- Refresh token rotation
- Blacklist management for revoked tokens

## Implementation

```typescript
// src/auth/JWTTokenManager.ts
import jwt from 'jsonwebtoken';
import { User } from '../types/User';

export class JWTTokenManager {
  private secretKey: string;
  private expiresIn: string;
  
  constructor() {
    // Configuration loaded from [[Configuration]]
    this.secretKey = process.env.JWT_SECRET!;
    this.expiresIn = process.env.JWT_EXPIRES_IN || '1h';
  }
  
  generateToken(user: User): string {
    const payload = {
      userId: user.id,
      email: user.email,
      roles: user.roles // Links to [[Role-Based Access Control]]
    };
    
    return jwt.sign(payload, this.secretKey, {
      expiresIn: this.expiresIn,
      issuer: 'my-app'
    });
  }
  
  validateToken(token: string): DecodedToken | null {
    try {
      const decoded = jwt.verify(token, this.secretKey);
      return decoded as DecodedToken;
    } catch (error) {
      // Error handling via [[Authentication Errors]]
      return null;
    }
  }
}
```

## Integration Points

- **Authentication**: Used by [[Authentication System]] for login
- **Middleware**: Validates tokens in [[Authentication Middleware]]
- **Frontend**: Token storage handled by [[Auth Context]]
- **Database**: Blacklist stored via [[Session Store]]

## Security Features

- Short-lived access tokens (1 hour default)
- Refresh token rotation for security
- Token blacklisting on logout
- Rate limiting on token generation

## Configuration

Token settings managed in [[Configuration]]:
- `JWT_SECRET` - Signing key
- `JWT_EXPIRES_IN` - Token lifetime
- `JWT_REFRESH_EXPIRES_IN` - Refresh token lifetime

#authentication #jwt #security #tokens
