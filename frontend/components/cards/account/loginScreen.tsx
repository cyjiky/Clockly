import React, { useState, useEffect, useRef } from "react";
import type { LoginBodyDTO } from "@/constants/props/authProps";
import type { ExtendedActionButtonsProps } from "@/constants/props/internProps";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  KeyboardAvoidingView,
  Platform,
  Modal,
  ScrollView,
  Alert,
  Pressable,
  Animated,
  Easing,
  Dimensions
} from 'react-native';

import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons'; 

import CreateSignInButtons from "@/components/buttons/welcomeButtons";
import { API_URL } from "@/constants/api";
import { StyledInput } from "@/constants/mainConst";

const { height: SCREEN_HEIGHT } = Dimensions.get('window');

export default function LoginScreen({ isOpen, onClose }: ExtendedActionButtonsProps) {

    const [formData, setFormData] = useState<LoginBodyDTO>({
        username: "",
        password: "",
    });

    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);

    const translateY = useRef(new Animated.Value(SCREEN_HEIGHT)).current;

    useEffect(() => {
        if (isOpen) {
        Animated.timing(translateY, {
            toValue: 0,
            duration: 350,
            easing: Easing.out(Easing.back(1)),
            useNativeDriver: true,
        }).start();
        }
    }, [isOpen]);

    const handleClose = () => {
        Animated.timing(translateY, {
        toValue: SCREEN_HEIGHT,
        duration: 300,
        easing: Easing.in(Easing.quad),
        useNativeDriver: true,
        }).start(() => {
        onClose();
        });
    };

    const handleChange = (field: keyof LoginBodyDTO, value: string) => {
        let newValue: string | null = value;
        setFormData((prev) => ({ ...prev, [field]: newValue }));
    };

    const handleSubmit = async () => {
        if (!formData.username || !formData.password) {
            Alert.alert("Required Fields", "Please fill in Username, Email, and Password.");
            return;
        }
            setLoading(true);
        try {
            const response = await fetch(`${API_URL}/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                const errorBody = await response.json();
                throw new Error("Failed to register");
            }
            onClose();
        } catch (error) {
            Alert.alert("Error", "Registration failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

  return (
    <Modal
        animationType="fade"
        transparent={true}
        visible={isOpen}
        onRequestClose={handleClose}
    >
        <View 
            className="flex-1 bg-black/60"
            style={{
                justifyContent: Platform.OS === 'web' ? 'center' : 'flex-end',
                alignItems: Platform.OS === 'web' ? 'center' : 'stretch',
            }}
        >
        <Pressable className="absolute inset-0" onPress={handleClose} />
        
        <Animated.View
          style={{
            transform: [{ translateY: translateY }],
            elevation: 10,
            shadowColor: '#000',
            shadowOffset: { width: 0, height: -4 },
            shadowOpacity: 0.15,
            shadowRadius: 12,
            width: Platform.OS === 'web' ? 450 : '100%',
            }}
            className="z-10 max-h-[90%]"
        >
          <View 
            className="w-full h-full bg-white overflow-hidden"
            style={{
              borderTopLeftRadius: 36,
              borderTopRightRadius: 36,
              borderBottomLeftRadius: Platform.OS === 'web' ? 36 : 0,
              borderBottomRightRadius: Platform.OS === 'web' ? 36 : 0,
            }}
          >
            <KeyboardAvoidingView
                behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
                className="w-full flex-1"
            >
                {Platform.OS !== 'web' && (
                    <View className="align-center items-center pt-3 pb-2">
                    <View className="w-16 h-1.5 bg-slate-200 rounded-full" />
                    </View>
                )}

              <TouchableOpacity 
                onPress={handleClose} 
                className="absolute top-5 right-5 z-20 bg-slate-100 p-2 rounded-full active:bg-slate-200"
              >
                <Ionicons name="close" size={20} color="#64748b" />
              </TouchableOpacity>

              <ScrollView 
                contentContainerStyle={{ flexGrow: 1, paddingHorizontal: 24, paddingBottom: 40, paddingTop: Platform.OS === 'web' ? 40 : 20 }} 
                showsVerticalScrollIndicator={false}
                keyboardShouldPersistTaps="handled"
              >
                
                <View className="mb-8 align-center items-center">
                  <View className="bg-indigo-50 p-4 rounded-3xl mb-4 border border-indigo-100">
                    <MaterialCommunityIcons name="account-plus-outline" size={32} color="#4f46e5" />
                  </View>
                  <Text className="text-3xl font-extrabold text-slate-950 mb-1 tracking-tight text-center">
                    Log in
                  </Text>
                  <Text className="text-base text-slate-500 leading-6 text-center px-4">
                    Please enter your details to continue
                  </Text>
                </View>

                <View className="flex-col">
                  <Text className="text-sm font-semibold text-slate-800 mb-2 ml-1">Account Details</Text>
                  
                  <StyledInput 
                    icon="person-outline"
                    placeholder="Username (unique)"
                    autoCapitalize="none"
                    value={formData.username}
                    onChangeText={(text: string) => handleChange("username", text)}
                  />

                  <Text className="text-sm font-semibold text-slate-800 mt-2 mb-2 ml-1">Personal Info</Text>

                  {/* Password */}
                  <View className="relative mb-6">
                    <View className="absolute left-4 top-[18px] z-10">
                      <Ionicons name="lock-closed-outline" size={20} color="#94a3b8" />
                    </View>
                    <TextInput
                      className="w-full bg-slate-50 border border-slate-200 focus:border-indigo-400 rounded-2xl pl-12 pr-14 py-4 text-slate-900 text-base shadow-sm shadow-black/5"
                      placeholder="••••••••"
                      placeholderTextColor="#94a3b8"
                      secureTextEntry={!showPassword}
                      value={formData.password}
                      onChangeText={(text) => handleChange("password", text)}
                      selectionColor="#4f46e5"
                      autoCapitalize="none"
                      autoCorrect={false}
                    />
                    <TouchableOpacity 
                      onPress={() => setShowPassword(!showPassword)} 
                      className="absolute right-0 top-0 bottom-0 px-4 justify-center"
                      activeOpacity={0.6}
                    >
                      <Ionicons 
                        name={showPassword ? "eye-off-outline" : "eye-outline"} 
                        size={22} 
                        color="#64748b" 
                      />
                    </TouchableOpacity>
                  </View>
                </View>

                <View className="flex-1 min-h-[32px]" />

                <CreateSignInButtons 
                  isOpen={isOpen} 
                  onClose={handleClose}
                  onSubmit={handleSubmit}
                />

              </ScrollView>
            </KeyboardAvoidingView>
          </View>
        </Animated.View>
      </View>
    </Modal>
  )
}