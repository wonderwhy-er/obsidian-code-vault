# Database Layer

Handles all data persistence operations using PostgreSQL with Prisma ORM.

## Architecture

```
┌─────────────────┐
│   Application   │
├─────────────────┤
│  Repository     │ ← [Repository Pattern](Repository%2520Pattern.md)
├─────────────────┤
│  Prisma Client  │ ← [ORM Configuration](ORM%2520Configuration.md)
├─────────────────┤
│  PostgreSQL     │
└─────────────────┘
```

## Key Components

- [Repository Pattern](Repository%2520Pattern.md) - Data access abstraction
- [Database Migrations](Database%2520Migrations.md) - Schema versioning
- [Connection Pooling](Connection%2520Pooling.md) - Performance optimization
- [Query Optimization](Query%2520Optimization.md) - Performance best practices

## Main Repositories

### UserRepository
```typescript
// Located in: src/repositories/UserRepository.ts
class UserRepository extends BaseRepository<User> {
  async findByEmail(email: string): Promise<User | null> {
    // Links to [User Management](User%2520Management.md) entity
  }
  
  async createUser(userData: CreateUserDto): Promise<User> {
    // Uses [Authentication System](Authentication%2520System.md) for password hashing
  }
}
```

### ProductRepository
```typescript
// Links to [Product Management](Product%2520Management.md) domain
class ProductRepository extends BaseRepository<Product> {
  async findWithCategories(): Promise<Product[]> {
    // Complex query examples in [Query Optimization](Query%2520Optimization.md)
  }
}
```

## Performance

- Connection pooling configured in [Configuration](../../05-operations/Configuration.md)
- Slow query monitoring via [Database Monitoring](Database%2520Monitoring.md)
- Caching strategy documented in [Caching Layer](Caching%2520Layer.md)

## Error Handling

- Database errors handled by [Database Error Handler](Database%2520Error%2520Handler.md)
- Transaction rollbacks in [Transaction Management](Transaction%2520Management.md)
- Connection failures managed by [Connection Resilience](Connection%2520Resilience.md)

#database #persistence #infrastructure
