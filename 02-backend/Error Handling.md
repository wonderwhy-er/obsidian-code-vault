# Error Handling

Centralized error handling patterns and error management across the application.

## Error Categories

### Application Errors
- **ValidationError** - Input validation failures
- **AuthenticationError** - Auth-related failures  
- **AuthorizationError** - Permission violations
- **NotFoundError** - Resource not found
- **ConflictError** - Business rule violations

### System Errors
- **DatabaseError** - Database connection/query issues
- **ExternalServiceError** - Third-party API failures
- **ConfigurationError** - Missing or invalid config

## Error Handler Middleware

```typescript
// src/middleware/errorHandler.ts
import { Request, Response, NextFunction } from 'express';
import { AppError } from '../types/errors';

export const errorHandler = (
  error: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  if (error instanceof AppError) {
    // Application errors - known and handled
    res.status(error.statusCode).json({
      success: false,
      message: error.message,
      code: error.code
    });
  } else {
    // System errors - log and return generic message
    console.error('Unexpected error:', error);
    res.status(500).json({
      success: false,
      message: 'Internal server error'
    });
  }
};
```

## Error Classes

```typescript
// src/types/errors.ts
export abstract class AppError extends Error {
  abstract statusCode: number;
  abstract code: string;
}

export class ValidationError extends AppError {
  statusCode = 400;
  code = 'VALIDATION_ERROR';
}

export class AuthenticationError extends AppError {
  statusCode = 401;
  code = 'AUTHENTICATION_ERROR';
}
```

## Integration Points

- **API Layer**: All routes use error middleware from [API Design](API%20Design.md)
- **Database**: Database errors handled in [Database Layer](Database%20Layer.md)
- **Auth**: Authentication errors in [Authentication System](Authentication%20System.md)
- **Frontend**: Error display in [Frontend Components](Frontend%20Components.md)

## Logging Strategy

Errors are logged with different levels:
- **Error**: System failures requiring immediate attention
- **Warn**: Business rule violations and validation errors
- **Info**: Expected errors like "user not found"

#error-handling #middleware #logging
