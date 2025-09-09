# Database Layer

Handles all data persistence operations using PostgreSQL with Prisma ORM.

## Architecture

```
┌─────────────────┐
│   Application   │
├─────────────────┤
│  Repository     │ ← [Repository Pattern](Repository%252520Pattern.md)
├─────────────────┤
│  Prisma Client  │ ← [ORM Configuration](ORM%252520Configuration.md)
├─────────────────┤
│  PostgreSQL     │
└─────────────────┘
```

## Key Components

- [Repository Pattern](Repository%252520Pattern.md) - Data access abstraction
- [Database Migrations](Database%252520Migrations.md) - Schema versioning
- [Connection Pooling](Connection%252520Pooling.md) - Performance optimization
- [Query Optimization](Query%252520Optimization.md) - Performance best practices

## Main Repositories

### UserRepository
```typescript
// Located in: src/repositories/UserRepository.ts
class UserRepository extends BaseRepository<User> {
  async findByEmail(email: string): Promise<User | null> {
    // Links to [User Management](User%252520Management.md) entity
  }
  
  async createUser(userData: CreateUserDto): Promise<User> {
    // Uses [Authentication System](Authentication%252520System.md) for password hashing
  }
}
```

### ProductRepository
```typescript
// Links to [Product Management](Product%252520Management.md) domain
class ProductRepository extends BaseRepository<Product> {
  async findWithCategories(): Promise<Product[]> {
    // Complex query examples in [Query Optimization](Query%252520Optimization.md)
  }
}
```

## Performance

- Connection pooling configured in [Configuration](../../05-operations/Configuration.md)
- Slow query monitoring via [Database Monitoring](Database%252520Monitoring.md)
- Caching strategy documented in [Caching Layer](Caching%252520Layer.md)

## Error Handling

- Database errors handled by [Database Error Handler](Database%252520Error%252520Handler.md)
- Transaction rollbacks in [Transaction Management](Transaction%252520Management.md)
- Connection failures managed by [Connection Resilience](Connection%252520Resilience.md)

#database #persistence #infrastructure
