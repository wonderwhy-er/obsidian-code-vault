# Database Layer

Handles all data persistence operations using PostgreSQL with Prisma ORM.

## Architecture

```
┌─────────────────┐
│   Application   │
├─────────────────┤
│  Repository     │ ← [[Repository Pattern]]
├─────────────────┤
│  Prisma Client  │ ← [[ORM Configuration]]
├─────────────────┤
│  PostgreSQL     │
└─────────────────┘
```

## Key Components

- [[Repository Pattern]] - Data access abstraction
- [[Database Migrations]] - Schema versioning
- [[Connection Pooling]] - Performance optimization
- [[Query Optimization]] - Performance best practices

## Main Repositories

### UserRepository
```typescript
// Located in: src/repositories/UserRepository.ts
class UserRepository extends BaseRepository<User> {
  async findByEmail(email: string): Promise<User | null> {
    // Links to [[User Management]] entity
  }
  
  async createUser(userData: CreateUserDto): Promise<User> {
    // Uses [[Authentication System]] for password hashing
  }
}
```

### ProductRepository
```typescript
// Links to [[Product Management]] domain
class ProductRepository extends BaseRepository<Product> {
  async findWithCategories(): Promise<Product[]> {
    // Complex query examples in [[Query Optimization]]
  }
}
```

## Performance

- Connection pooling configured in [[Configuration]]
- Slow query monitoring via [[Database Monitoring]]
- Caching strategy documented in [[Caching Layer]]

## Error Handling

- Database errors handled by [[Database Error Handler]]
- Transaction rollbacks in [[Transaction Management]]
- Connection failures managed by [[Connection Resilience]]

#database #persistence #infrastructure
