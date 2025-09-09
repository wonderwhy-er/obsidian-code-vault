# Configuration

Environment configuration and application settings management.

## Configuration Structure

```
config/
├── development.json
├── staging.json
├── production.json
└── default.json
```

## Environment Variables

### Database Configuration
```bash
# Database connection - used by [[Database Layer]]
DATABASE_URL=postgresql://user:pass@localhost:5432/myapp
DB_POOL_MIN=2
DB_POOL_MAX=10
```

### Authentication Settings
```bash
# JWT configuration - used by [[JWT Token Manager]]
JWT_SECRET=your-super-secret-key
JWT_EXPIRES_IN=1h
JWT_REFRESH_EXPIRES_IN=7d

# Password policy - used by [[Password Hashing]]
MIN_PASSWORD_LENGTH=8
PASSWORD_REQUIRE_SPECIAL_CHARS=true
```

### API Configuration
```bash
# Server settings - used by [[API Design]]
PORT=3000
API_VERSION=v1
CORS_ORIGIN=http://localhost:3001

# Rate limiting - used by [[Rate Limiting]]
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

## Configuration Loading

```typescript
// src/config/index.ts
import dotenv from 'dotenv';

export interface AppConfig {
  port: number;
  database: DatabaseConfig;
  jwt: JWTConfig;
  api: APIConfig;
}

export const loadConfig = (): AppConfig => {
  dotenv.config();
  
  return {
    port: parseInt(process.env.PORT || '3000'),
    database: {
      url: process.env.DATABASE_URL!,
      poolMin: parseInt(process.env.DB_POOL_MIN || '2'),
      poolMax: parseInt(process.env.DB_POOL_MAX || '10')
    },
    jwt: {
      secret: process.env.JWT_SECRET!,
      expiresIn: process.env.JWT_EXPIRES_IN || '1h'
    }
  };
};
```

## Usage Across System

- **Database**: Connection settings in [[Database Layer]]
- **Auth**: Token configuration in [[Authentication System]]
- **API**: Server and middleware settings in [[API Design]]
- **Testing**: Test-specific overrides in [[Testing Strategy]]

#configuration #environment #settings
