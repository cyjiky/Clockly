import { View, Text, TouchableOpacity } from 'react-native'
import type { ExtendedActionButtonsProps } from '@/constants/props/internProps'

import { ChevronLeft, Search, Plus, AlignJustify } from 'lucide-react-native'; 

export default function CreateSignInButtons(
    { isOpen, onClose, onSubmit }: ExtendedActionButtonsProps
) {
    return (
        <View className='mt-auto pt-6'>
            
            <TouchableOpacity
                activeOpacity={0.8}
                className='w-full bg-indigo-600 py-4 rounded-2xl 
                  items-center shadow-sm mb-6'
                onPress={onSubmit}
            >
                <Text className='text-white text-lg font-bold'>
                    Create Account 
                </Text>
            </TouchableOpacity>

            <View className="flex-row items-center bg-white rounded-full px-5 py-2.5 shadow-sm shadow-black/10 gap-6">
        
                <TouchableOpacity 
                    activeOpacity={0.7} 
                    onPress={onSubmit}
                >
                    <AlignJustify 
                        color="#000" 
                        size={24} 
                        strokeWidth={2.5} 
                    />
                </TouchableOpacity>

                <TouchableOpacity 
                    activeOpacity={0.7} 
                    onPress={onSubmit}
                >
                    <Search 
                        color="#000" 
                        size={24} 
                        strokeWidth={2.5} 
                    />
                </TouchableOpacity>

                <TouchableOpacity 
                    activeOpacity={0.7} 
                    onPress={onSubmit}
                >
                    <Plus 
                        color="#000" 
                        size={28} 
                        strokeWidth={2.5} 
                    />
                </TouchableOpacity>
        
            </View>

        </View>
    )
}