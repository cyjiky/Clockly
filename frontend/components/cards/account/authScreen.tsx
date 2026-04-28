import React, { useState } from 'react'
import { View } from 'react-native'

import WelcomeScreen from './welcomeScreen'
import RegisterScreen from './registerScreen'
import LoginScreen from './loginScreen'

export default function AuthScreen() {
    const [
        activeCard, setActiveCard
    ] = useState<'none' | 'login' | 'register'>('none');

    return (
        <View>

            <WelcomeScreen
                onNavigateToLogin={() => setActiveCard('login')}
                onNavigateToRegister={() => setActiveCard('register')}
            />

            <RegisterScreen
                isOpen={activeCard === 'register'}
                onClose={() => setActiveCard('none')}
            />

            <LoginScreen
                isOpen={activeCard === 'login'}
                onClose={() => setActiveCard('none')}
            />
            
        </View>
    )
}