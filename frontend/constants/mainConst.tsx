import { View, TextInput } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

export const StyledInput = ({ icon, placeholder, value, onChangeText, ...props }: any) => (
    <View className='relative mb-4'>

        <View className='absolute left-4 top-[18px] z-10'>
            <Ionicons name={icon} size={20} color='#94a3b8' />
        </View>

        <TextInput
            className='w-full bg-slate-50 border border-slate-200
            focus:border-indigo-400 rounded-2xl pl-12 pr-5 py-4
            text-slate-900 text-base shadow-sm shadow-black/5'
            placeholder={placeholder}
            placeholderTextColor='#94a3b8'
            value={value}
            onChangeText={onChangeText}
            selectionColor='#4f46e5'
            autoCorrect={false}
            {...props}
        />

    </View>
)