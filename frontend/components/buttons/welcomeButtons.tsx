import { View, Text, TouchableOpacity } from 'react-native'
import type { ExtendedActionButtonsProps } from '@/constants/props/internProps'

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

            <View className='flex-row justify-center items-center'>
                <Text className='text-slate-500 text-base'>
                    Already have an account?{'  '}
                </Text>
                <TouchableOpacity
                    activeOpacity={0.6}
                    onPress={onSubmit}
                >
                    <Text className='text-indigo-600 text-base font-bold'>
                        Sign in
                    </Text>
                </TouchableOpacity>
            </View>

        </View>
    )
}