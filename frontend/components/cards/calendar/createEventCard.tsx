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
  Dimensions,
  Switch
} from 'react-native';

import { API_URL } from "@/constants/api";
import type { EventProps } from "@/constants/props/calendarProps";

const { height: SCREEN_HEIGHT } = Dimensions.get('window');

export default function CreateEventCard({ isOpen, onClose }: ExtendedActionButtonsProps) {

    // TODO 
    const [location, setLocation] = useState('');
    const [isAllDay, setIsAllDay] = useState(false);
    
    const [formData, setFormData] = useState<EventProps>({
        name: "",
        description: "",
        start_date: null,
        end_date: null,
        repeat_days: [""],
    });

    const [loading, setLoading] = useState(false);

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

    const handleChange = (field: keyof EventProps, value: string) => {
        let newValue: string | null = value;
        setFormData((prev) => ({ ...prev, [field]: newValue }));
    };

    const handleSubmit = async () => {
        try {
            const response = await fetch(`${API_URL}/object/{time_object_type}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                const errorBody = await response.json();
                throw new Error("Failed to create event");
            }
            onClose();
        } catch (error) {
            Alert.alert("Error", "Event creation failed. Please try again.");
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

              <ScrollView 
                contentContainerStyle={{ flexGrow: 1, paddingHorizontal: 24, paddingBottom: 40, paddingTop: Platform.OS === 'web' ? 40 : 20 }} 
                showsVerticalScrollIndicator={false}
                keyboardShouldPersistTaps="handled"
              >
                
                <View className="flex-row justify-between items-center px-5 pt-3 pb-4">
                    <TouchableOpacity activeOpacity={0.7} onPress={handleClose} >
                        <Text className="text-[#007AFF] text-lg">Cancel</Text>
                    </TouchableOpacity>

                    <Text className="text-black text-lg font-semibold">New Event</Text>
                    
                    <TouchableOpacity activeOpacity={0.7} onPress={handleSubmit}>
                        <Text className="text-[#007AFF] text-lg font-semibold">Add</Text>
                    </TouchableOpacity>
                </View>

                <View className="bg-white rounded-2xl mx-4 mt-2 overflow-hidden shadow-sm">
                    <TextInput
                        className="px-4 py-4 text-base text-black"
                        placeholder="Title"
                        placeholderTextColor="#8E8E93"
                        value={formData.name}
                        onChangeText={(text: string) => handleChange("name", text)}
                    />
                    <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />
                    <TextInput
                        className="px-4 py-4 text-base text-black"
                        placeholder="Location or Video Call"
                        placeholderTextColor="#8E8E93"
                        value={location}
                        onChangeText={setLocation}
                    />
                </View>

                <View className="bg-white rounded-2xl mx-4 mt-6 overflow-hidden shadow-sm">
                    <View className="flex-row justify-between items-center px-4 py-3">
                        <Text className="text-base text-black">All-day</Text>
                        <Switch
                            value={isAllDay}
                            onValueChange={setIsAllDay}
                            trackColor={{ true: '#34C759', false: '#E9E9EA' }}
                        />
                    </View>

                    <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />

                    <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
                        <Text className="text-base text-black">Starts</Text>
                        <View className="flex-row items-center gap-2">
                            <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                                May 5, 2026
                            </Text>
                            {!isAllDay && (
                                <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                                    9:00 PM
                                </Text>
                            )}
                        </View>
                    </TouchableOpacity>

                    <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />

                    <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
                        <Text className="text-base text-black">Ends</Text>
                        <View className="flex-row items-center gap-2">
                            <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                                May 5, 2026
                            </Text>
                            {!isAllDay && (
                                <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                                    10:00 PM
                                </Text>
                            )}
                        </View>
                    </TouchableOpacity>
                </View>

                <View className="bg-white rounded-2xl mx-4 mt-6 overflow-hidden shadow-sm">
                    <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
                        <Text className="text-base text-black">Repeat</Text>
                        <View className="flex-row items-center">
                            <Text className="text-base text-[#8E8E93] mr-2">Never</Text>
                            <Text className="text-[#C6C6C8] text-xl font-medium">›</Text>
                        </View>
                    </TouchableOpacity>

                    <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />

                    <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
                        <Text className="text-base text-black">Alert</Text>
                        <View className="flex-row items-center">
                            <Text className="text-base text-[#8E8E93] mr-2">10 minutes before</Text>
                            <Text className="text-[#C6C6C8] text-xl font-medium">›</Text>
                        </View>
                    </TouchableOpacity>
                </View>

                <View className="bg-white rounded-2xl mx-4 mt-6 mb-6 overflow-hidden shadow-sm">
                    <TextInput
                        className="px-4 py-4 text-base text-black min-h-[120px]"
                        placeholder="Description"
                        placeholderTextColor="#8E8E93"
                        multiline={true}
                        textAlignVertical="top"
                        value={formData.description}
                        onChangeText={(text: string) => handleChange("description", text)}
                    />
                </View>

              </ScrollView>
            </KeyboardAvoidingView>
          </View>
        </Animated.View>
      </View>
    </Modal>
  )
}