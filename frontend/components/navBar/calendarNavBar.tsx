import { View, Text } from 'react-native'
import TodayButton from '../buttons/todayButton'
import SearchButton from '../buttons/searchButton'

export default function CalendarNavbar(){
    return (
        <View className='flex-row justify-between items-center 
          px-16 py-12 bg-white border-b border-slate-200'
        >
            <Text className='text-slate-500 text-lg font-medium uppercase tracking-wider'>
                Menu
            </Text>

            <TodayButton/>
            <SearchButton/>

        </View>
    )
}