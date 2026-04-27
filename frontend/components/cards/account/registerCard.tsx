import React, { useState } from 'react';
import { RegisterBodyDTO } from '@/constants/props/authProps';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  KeyboardAvoidingView,
  Platform,
  SafeAreaView,
  TouchableWithoutFeedback,
  Keyboard,
} from 'react-native';

// TODO
const RegisterScreen = ({ isOpen, setClose}: RegisterBodyDTO) => {
    // const [ isOpen, setClose ] = useState(setClose)<RegisterBodyDTO>;
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    return (
        <SafeAreaView className="flex-1 bg-white">
            <KeyboardAvoidingView
                behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
                className="flex-1 justify-center px-6"
            >
                <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
                <View>
                    
                    <Text className="text-3xl font-bold text-gray-900 mb-2 text-center">
                    Create an acctount
                    </Text>
                    <Text className="text-gray-500 text-center mb-8 text-base">
                    Please fill in your details to register.
                    </Text>

                    <View className="space-y-4">
                    
                    {/* Name */}
                    <View>
                        <Text className="text-gray-700 font-medium mb-1 ml-1">Name</Text>
                        <TextInput
                        className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 text-base"
                        placeholder="John"
                        placeholderTextColor="#9ca3af"
                        value={name}
                        onChangeText={setName}
                        />
                    </View>

                    {/* Email */}
                    <View>
                        <Text className="text-gray-700 font-medium mb-1 ml-1">Email</Text>
                        <TextInput
                        className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 text-base"
                        placeholder="example@mail.com"
                        placeholderTextColor="#9ca3af"
                        keyboardType="email-address"
                        autoCapitalize="none"
                        value={email}
                        onChangeText={setEmail}
                        />
                    </View>

                    {/* Password */}
                    <View>
                        <Text className="text-gray-700 font-medium mb-1 ml-1">Password</Text>
                        <TextInput
                        className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 text-base"
                        placeholder="••••••••"
                        placeholderTextColor="#9ca3af"
                        secureTextEntry
                        value={password}
                        onChangeText={setPassword}
                        />
                    </View>

                    {/* Password 2 */}
                    <View>
                        <Text className="text-gray-700 font-medium mb-1 ml-1">Password 2</Text>
                        <TextInput
                        className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 text-base"
                        placeholder="••••••••"
                        placeholderTextColor="#9ca3af"
                        secureTextEntry
                        value={confirmPassword}
                        onChangeText={setConfirmPassword}
                        />
                    </View>
                    
                    </View>

                    {/* Buttons */}
                    <TouchableOpacity
                    className="bg-blue-600 rounded-xl py-4 mt-8 items-center active:bg-blue-700"
                    onPress={handleRegister}
                    >
                    <Text className="text-white text-lg font-bold">Create an account</Text>
                    </TouchableOpacity>

                    <View className="flex-row justify-center mt-6">
                    <Text className="text-gray-500 text-base">Already have an account? </Text>
                    <TouchableOpacity>
                        <Text className="text-blue-600 text-base font-bold">Log In</Text>
                    </TouchableOpacity>
                    </View>

                </View>
                </TouchableWithoutFeedback>
            </KeyboardAvoidingView>
        </SafeAreaView>
    );
};

export default RegisterScreen;