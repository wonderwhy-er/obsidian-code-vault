# Frontend Components

React component library and UI patterns for the application.

## Component Hierarchy

```
App
├── Layout/
│   ├── [[Header Component]]
│   ├── [[Navigation Component]]
│   └── [[Footer Component]]
├── Auth/
│   ├── [[Login Component]]
│   ├── [[Register Component]]
│   └── [[Protected Route]]
├── User/
│   ├── [[User Profile]]
│   ├── [[User Settings]]
│   └── [[User Dashboard]]
└── Common/
    ├── [[Button Component]]
    ├── [[Input Component]]
    └── [[Modal Component]]
```

## State Management

- Global state via [[Redux Store]]
- Authentication state in [[Auth Context]]
- API calls through [[React Query]]
- Form state with [[Form Validation]]

## Key Components

### Login Component
```jsx
// src/components/Auth/LoginComponent.tsx
import { AuthService } from '../../services/AuthService';
import { useAuth } from '../hooks/useAuth'; // Links to [[Auth Context]]

export const LoginComponent = () => {
  // Integrates with [[Authentication System]]
  // Uses [[Input Component]] for form fields
  // Handles [[Authentication Errors]]
};
```

### Protected Route
```jsx
// Higher-order component for route protection
// Links to [[Authentication System]] for validation
// Redirects via [[Navigation Component]] patterns
```

## Styling

- Design system documented in [[Design Tokens]]
- Component styles in [[Styled Components]]
- Responsive design via [[Media Queries]]

#frontend #react #components #ui
