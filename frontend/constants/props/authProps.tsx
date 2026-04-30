export interface JWTTokenProps {
  access_token: string;
  refresh_token: string;
}

export interface WelcomeScreenProps {
  onNavigateToLogin?: () => void;
  onNavigateToRegister?: () => void;
}

// TODO 
export interface RegisterBodyDTO{
  username: string;
  email: string;
  password: string;
}

export interface LoginBodyDTO {
  username: string;
  password: string;
}