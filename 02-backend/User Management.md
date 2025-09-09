# User Management

Core user operations and data management across the application.

## Overview

Handles user lifecycle from registration to account deletion, including profile management and user data operations.

## Key Operations

- User registration and onboarding
- Profile updates and data management
- Account deactivation and deletion
- User search and listing (admin)

## Data Model

```typescript
// src/types/User.ts
interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  roles: Role[]; // Links to [Role-Based Access Control](Role-Based%2520Access%2520Control.md)
  createdAt: Date;
  updatedAt: Date;
  lastLoginAt?: Date;
  isActive: boolean;
}
```

## Core Services

### UserService
```typescript
// src/services/UserService.ts
export class UserService {
  constructor(
    private userRepository: UserRepository, // [Database Layer](Database%2520Layer.md)
    private authService: AuthService        // [Authentication System](Authentication%2520System.md)
  ) {}
  
  async createUser(userData: CreateUserDto): Promise<User> {
    // Password hashing via [Password Hashing](Password%2520Hashing.md)
    // Email validation and uniqueness check
    // Initial role assignment
  }
  
  async updateProfile(userId: string, updates: UpdateUserDto): Promise<User> {
    // Profile validation
    // Change tracking for audit
  }
}
```

## Related Components

- **Frontend**: [User Profile](User%2520Profile.md), [User Dashboard](User%2520Dashboard.md)
- **API**: User endpoints in [API Design](API%2520Design.md)
- **Database**: [UserRepository](UserRepository.md) in [Database Layer](Database%2520Layer.md)
- **Auth**: Integration with [Authentication System](Authentication%2520System.md)

## Business Rules

- Email must be unique across system
- Users can update their own profiles
- Admins can manage all user accounts
- Soft deletion preserves audit trail

#users #core-domain #user-management
