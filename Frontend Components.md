# Frontend Components

React component library and UI patterns for the application.

## Component Hierarchy

```
App
├── Layout/
│   ├── [Header Component](Header%2520Component.md)
│   ├── [Navigation Component](Navigation%2520Component.md)
│   └── [Footer Component](Footer%2520Component.md)
├── Auth/
│   ├── [Login Component](Login%2520Component.md)
│   ├── [Register Component](Register%2520Component.md)
│   └── [Protected Route](Protected%2520Route.md)
├── User/
│   ├── [User Profile](User%2520Profile.md)
│   ├── [User Settings](User%2520Settings.md)
│   └── [User Dashboard](User%2520Dashboard.md)
└── Common/
    ├── [Button Component](Button%2520Component.md)
    ├── [Input Component](Input%2520Component.md)
    └── [Modal Component](Modal%2520Component.md)
```

## State Management

- Global state via [Redux Store](Redux%2520Store.md)
- Authentication state in [Auth Context](Auth%2520Context.md)
- API calls through [React Query](React%2520Query.md)
- Form state with [Form Validation](Form%2520Validation.md)

## Key Components

### Login Component
```jsx
// src/components/Auth/LoginComponent.tsx
import { AuthService } from '../../services/AuthService';
import { useAuth } from '../hooks/useAuth'; // Links to [Auth Context](Auth%2520Context.md)

export const LoginComponent = () => {
  // Integrates with [Authentication System](Authentication%2520System.md)
  // Uses [Input Component](Input%2520Component.md) for form fields
  // Handles [Authentication Errors](Authentication%2520Errors.md)
};
```

### Protected Route
```jsx
// Higher-order component for route protection
// Links to [Authentication System](Authentication%2520System.md) for validation
// Redirects via [Navigation Component](Navigation%2520Component.md) patterns
```

## Styling

- Design system documented in [Design Tokens](Design%2520Tokens.md)
- Component styles in [Styled Components](Styled%2520Components.md)
- Responsive design via [Media Queries](Media%2520Queries.md)

#frontend #react #components #ui
