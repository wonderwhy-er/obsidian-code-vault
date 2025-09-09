# Frontend Components

React component library and UI patterns for the application.

## Component Hierarchy

```
App
├── Layout/
│   ├── [Header Component](Header%20Component.md)
│   ├── [Navigation Component](Navigation%20Component.md)
│   └── [Footer Component](Footer%20Component.md)
├── Auth/
│   ├── [Login Component](Login%20Component.md)
│   ├── [Register Component](Register%20Component.md)
│   └── [Protected Route](Protected%20Route.md)
├── User/
│   ├── [User Profile](User%20Profile.md)
│   ├── [User Settings](User%20Settings.md)
│   └── [User Dashboard](User%20Dashboard.md)
└── Common/
    ├── [Button Component](Button%20Component.md)
    ├── [Input Component](Input%20Component.md)
    └── [Modal Component](Modal%20Component.md)
```

## State Management

- Global state via [Redux Store](Redux%20Store.md)
- Authentication state in [Auth Context](Auth%20Context.md)
- API calls through [React Query](React%20Query.md)
- Form state with [Form Validation](Form%20Validation.md)

## Key Components

### Login Component
```jsx
// src/components/Auth/LoginComponent.tsx
import { AuthService } from '../../services/AuthService';
import { useAuth } from '../hooks/useAuth'; // Links to [Auth Context](Auth%20Context.md)

export const LoginComponent = () => {
  // Integrates with [Authentication System](Authentication%20System.md)
  // Uses [Input Component](Input%20Component.md) for form fields
  // Handles [Authentication Errors](Authentication%20Errors.md)
};
```

### Protected Route
```jsx
// Higher-order component for route protection
// Links to [Authentication System](Authentication%20System.md) for validation
// Redirects via [Navigation Component](Navigation%20Component.md) patterns
```

## Styling

- Design system documented in [Design Tokens](Design%20Tokens.md)
- Component styles in [Styled Components](Styled%20Components.md)
- Responsive design via [Media Queries](Media%20Queries.md)

#frontend #react #components #ui
