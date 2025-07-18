# Gately SDK Documentation

A comprehensive documentation site for the Gately SDK, built with React, TypeScript, and Tailwind CSS. This documentation provides complete guides, examples, and API references for integrating Gately authentication and user management into your applications.

## 🚀 Features

### **Modern Design**

- **Dark Mode Support**: Pure black dark mode with excellent contrast
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Custom Color Scheme**: Uses Gately brand colors (#FFC599 accent)
- **Onest Font**: Modern, readable typography

### **Complete Documentation**

- **Getting Started**: Installation and quick start guides
- **Core Features**: Authentication, user management, SSO, forms, plans
- **Framework Support**: React, Vue, Svelte, Angular, and Framer integration
- **API Reference**: Complete method documentation
- **Examples**: Real-world code examples and use cases

### **Interactive Components**

- **Code Blocks**: Syntax-highlighted code examples
- **Live Examples**: Interactive demonstration components
- **Search Functionality**: Find documentation quickly
- **Navigation**: Sidebar with organized sections

## 🛠️ Tech Stack

- **Framework**: React 19 \+ TypeScript
- **Styling**: Tailwind CSS with custom design system
- **Routing**: React Router DOM
- **Icons**: Lucide React
- **Build Tool**: Vite
- **Fonts**: Onest (primary), JetBrains Mono (code)

## 📦 Installation

### Prerequisites

- Node.js 18\+
- npm or pnpm

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd GatelySDK/sdk-docs

# Install dependencies
npm install

# Start development server
npm run dev
```

The documentation will be available at `http://localhost:5173`

## 🎨 Design System

### Color Palette

```css
/* Primary Colors */
--accent-300: #FFC599;  /* Main accent color */
--accent-400: #FFB17A;  /* Hover states */

/* Gray Scale */
--gray-50: #f9fafb;     /* Light backgrounds */
--gray-900: #111827;    /* Dark backgrounds */
--gray-950: #030712;    /* Pure black (dark mode) */
```

### Typography

- **Primary Font**: Onest (400, 500, 600, 700)
- **Code Font**: JetBrains Mono (400, 500, 600)
- **Fallback**: Inter, system-ui

### Dark Mode

- **Background**: Pure black (`gray-950`)
- **Cards**: Very dark gray (`gray-900`)
- **Text**: White and light gray shades
- **Borders**: Dark gray (`gray-700`)

## 📁 Project Structure

```
sdk-docs/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── CodeBlock.tsx   # Syntax-highlighted code
│   │   ├── DarkModeToggle.tsx
│   │   ├── Header.tsx      # Top navigation
│   │   └── Sidebar.tsx     # Left navigation
│   ├── pages/              # Documentation pages
│   │   ├── Home.tsx        # Landing page
│   │   ├── Installation.tsx
│   │   ├── Authentication.tsx
│   │   ├── UserManagement.tsx
│   │   ├── SSO.tsx
│   │   ├── UIComponents.tsx
│   │   ├── Forms.tsx
│   │   ├── Plans.tsx
│   │   ├── FrameworkAdapters.tsx
│   │   ├── Framer.tsx      # Framer integration
│   │   ├── APIReference.tsx
│   │   └── Examples.tsx
│   ├── App.tsx             # Main app component
│   ├── main.tsx           # Entry point
│   └── index.css          # Global styles
├── public/                # Static assets
│   └── Icon.svg          # Gately logo
├── tailwind.config.js    # Tailwind configuration
├── package.json          # Dependencies
└── README.md            # This file
```

## 🎯 Available Scripts

```bash
# Development
npm run dev              # Start development server
npm run build            # Build for production
npm run preview          # Preview production build
npm run lint             # Run ESLint

# Type checking
npm run typecheck        # Check TypeScript types
```

## 📚 Documentation Sections

### **Getting Started**

- Introduction to Gately SDK
- Installation guide
- Quick start examples

### **Core Features**

- **Authentication**: Email/password, magic links, SSO
- **User Management**: Profiles, roles, permissions
- **SSO Integration**: Google, GitHub, custom providers
- **UI Components**: Pre-built authentication components
- **Forms**: Custom form handling and validation
- **Plans & Tiers**: Subscription and membership management

### **Framework Support**

- **Framework Adapters**: React, Vue, Svelte, Angular
- **Framer Integration**: No-code authentication in Framer

### **Reference**

- **API Reference**: Complete method documentation
- **Examples**: Real-world implementation examples

## 🎨 Customization

### Adding New Pages

1. Create a new component in `src/pages/`
2. Add the route to `src/App.tsx`
3. Add a navigation item to `src/components/Sidebar.tsx`

### Styling

- Use Tailwind CSS classes for styling
- Follow the established color scheme
- Use the accent color (`accent-300`) for highlights
- Ensure dark mode compatibility

### Code Examples

Use the `CodeBlock` component for syntax-highlighted code:

```tsx
<CodeBlock
  code={`// Your code here`}
  language="javascript"
  title="Example Title"
/>
```

## 🚀 Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Netlify

```bash
# Build the project
npm run build

# Deploy the dist folder
```

### Manual Deployment

```bash
# Build for production
npm run build

# Serve the dist folder with any static server
npx serve dist
```

## 🔧 Development

### Adding New Features

1. Create feature branch
2. Implement changes
3. Test in development
4. Update documentation
5. Submit pull request

### Code Style

- Use TypeScript for all components
- Follow React best practices
- Use functional components with hooks
- Maintain consistent naming conventions

### Testing

- Test all pages in both light and dark modes
- Verify responsive design on different screen sizes
- Check accessibility with screen readers
- Validate all code examples

## 🎨 Design Guidelines

### Color Usage

- **Primary Actions**: Use `accent-300` (#FFC599)
- **Backgrounds**: Use gray scale (50-950)
- **Text**: Use appropriate contrast ratios
- **Borders**: Use gray scale for subtle separation

### Typography

- **Headings**: Use Onest font with appropriate weights
- **Body Text**: Use Onest for readability
- **Code**: Use JetBrains Mono for code blocks

### Spacing

- Use Tailwind's spacing scale consistently
- Maintain proper visual hierarchy
- Ensure adequate white space

## 📱 Responsive Design

The documentation is fully responsive with breakpoints:

- **Mobile**: \< 768px
- **Tablet**: 768px - 1024px
- **Desktop**: \> 1024px

### Mobile Features

- Collapsible sidebar
- Touch-friendly navigation
- Optimized code blocks
- Readable typography

## 🌙 Dark Mode

### Implementation

- Uses CSS custom properties
- Tailwind's `dark:` prefix
- Smooth transitions
- Persistent user preference

### Color Mapping

- Light backgrounds → Dark backgrounds
- Dark text → Light text
- Maintains contrast ratios
- Uses pure black for main backgrounds

## 🔍 Search & Navigation

### Search Features

- Real-time search through documentation
- Keyboard shortcuts (Ctrl/Cmd \+ K)
- Search result highlighting

### Navigation

- Sidebar with organized sections
- Breadcrumb navigation
- Previous/Next page links
- Table of contents

## 📊 Performance

### Optimization

- Code splitting with React Router
- Optimized images and assets
- Efficient CSS with Tailwind
- Fast build times with Vite

### Metrics

- Lighthouse score: 95\+
- First Contentful Paint: \< 1.5s
- Largest Contentful Paint: \< 2.5s

## 🤝 Contributing

### Guidelines

1. Follow the existing code style
2. Add tests for new features
3. Update documentation
4. Test in both light and dark modes
5. Ensure accessibility compliance

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This documentation is part of the Gately SDK project and follows the same license terms.

## 🆘 Support

For issues with the documentation:

1. Check existing issues
2. Create a new issue with details
3. Include screenshots if relevant
4. Specify browser and device information

For SDK-related questions:

- Check the [Gately Documentation](https://usegately.com)
- Visit the [GitHub Repository](https://github.com/gately/sdk)
- Contact support through the Gately platform

---

**Built with ❤️ by the Gately Team**