# Frontend Components

React component library and UI patterns for the application.

## Component Hierarchy

```
App
├── Layout/
│   ├── [Header Component](Header%252520Component.md)
│   ├── [Navigation Component](Navigation%252520Component.md)
│   └── [Footer Component](Footer%252520Component.md)
├── Auth/
│   ├── [Login Component](Login%252520Component.md)
│   ├── [Register Component](Register%252520Component.md)
│   └── [Protected Route](Protected%252520Route.md)
├── User/
│   ├── [User Profile](User%252520Profile.md)
│   ├── [User Settings](User%252520Settings.md)
│   └── [User Dashboard](User%252520Dashboard.md)
└── Common/
    ├── [Button Component](Button%252520Component.md)
    ├── [Input Component](Input%252520Component.md)
    └── [Modal Component](Modal%252520Component.md)
```

## State Management

- Global state via [Redux Store](Redux%252520Store.md)
- Authentication state in [Auth Context](Auth%252520Context.md)
- API calls through [React Query](React%252520Query.md)
- Form state with [Form Validation](Form%252520Validation.md)

## Key Components

### Login Component
```jsx
// src/components/Auth/LoginComponent.tsx
import { AuthService } from '../../services/AuthService';
import { useAuth } from '../hooks/useAuth'; // Links to [Auth Context](Auth%252520Context.md)

export const LoginComponent = () => {
  // Integrates with [Authentication System](Authentication%252520System.md)
  // Uses [Input Component](Input%252520Component.md) for form fields
  // Handles [Authentication Errors](Authentication%252520Errors.md)
};
```

### Protected Route
```jsx
// Higher-order component for route protection
// Links to [Authentication System](Authentication%252520System.md) for validation
// Redirects via [Navigation Component](Navigation%252520Component.md) patterns
```

## Styling

- Design system documented in [Design Tokens](Design%252520Tokens.md)
- Component styles in [Styled Components](Styled%252520Components.md)
- Responsive design via [Media Queries](Media%252520Queries.md)

#frontend #react #components #ui
