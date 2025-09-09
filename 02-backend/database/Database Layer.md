# Database Layer

Handles all data persistence operations using PostgreSQL with Prisma ORM.

## Architecture

```
┌─────────────────┐
│   Application   │
├─────────────────┤
│  Repository     │ ← [Repository Pattern](Repository%20Pattern.md)
├─────────────────┤
│  Prisma Client  │ ← [ORM Configuration](ORM%20Configuration.md)
├─────────────────┤
│  PostgreSQL     │
└─────────────────┘
```

## Key Components

- [Repository Pattern](Repository%20Pattern.md) - Data access abstraction
- [Database Migrations](Database%20Migrations.md) - Schema versioning
- [Connection Pooling](Connection%20Pooling.md) - Performance optimization
- [Query Optimization](Query%20Optimization.md) - Performance best practices

## Main Repositories

### UserRepository
```typescript
// Located in: src/repositories/UserRepository.ts
class UserRepository extends BaseRepository<User> {
  async findByEmail(email: string): Promise<User | null> {
    // Links to [User Management](User%20Management.md) entity
  }
  
  async createUser(userData: CreateUserDto): Promise<User> {
    // Uses [Authentication System](Authentication%20System.md) for password hashing
  }
}
```

### ProductRepository
```typescript
// Links to [Product Management](Product%20Management.md) domain
class ProductRepository extends BaseRepository<Product> {
  async findWithCategories(): Promise<Product[]> {
    // Complex query examples in [Query Optimization](Query%20Optimization.md)
  }
}
```

## Performance

- Connection pooling configured in [Configuration](../../05-operations/Configuration.md)
- Slow query monitoring via [Database Monitoring](Database%20Monitoring.md)
- Caching strategy documented in [Caching Layer](Caching%20Layer.md)

## Error Handling

- Database errors handled by [Database Error Handler](Database%20Error%20Handler.md)
- Transaction rollbacks in [Transaction Management](Transaction%20Management.md)
- Connection failures managed by [Connection Resilience](Connection%20Resilience.md)

#database #persistence #infrastructure
