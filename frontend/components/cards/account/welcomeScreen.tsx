import React from 'react';
import { View, Text, TouchableOpacity, SafeAreaView } from 'react-native';
import { WelcomeScreenProps } from '@/constants/props/authProps';

const WelcomeScreen: React.FC<WelcomeScreenProps> = ({
  onNavigateToLogin,
  onNavigateToRegister,
}) => {
  return (
    <SafeAreaView className="flex-1 bg-white">
      <View className="flex-1 px-6 justify-center items-center">
        
        <View className="items-center mb-16">
          <Text className="text-5xl font-extrabold text-blue-600 mb-4 tracking-tight">
            Clockly
          </Text>
          <Text className="text-base text-gray-500 text-center px-4 leading-6">
            Welcome! To get started, create a new account or log in to an existing one 
          </Text>
        </View>

        <View className="w-full mt-8">
          <TouchableOpacity
            activeOpacity={0.8}
            onPress={onNavigateToRegister}
            className="w-full bg-indigo-700 py-4 rounded-2xl items-center shadow-sm mb-4"
          >
            <Text className="text-white text-lg font-bold">
              Create an account
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            activeOpacity={0.8}
            onPress={onNavigateToLogin}
            className="w-full bg-indigo-50 py-4 rounded-2xl items-center"
          >
            <Text className="text-indigo-700 text-lg font-bold">
              Log in 
            </Text>
          </TouchableOpacity>
        </View>

      </View>
    </SafeAreaView>
  );
};

export default WelcomeScreen;