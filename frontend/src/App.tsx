import s from './App.module.scss'
import { MainRoutes } from './layouts/MainRoutes/MainRoutes'
import './assets/styles/reset.css'
import './assets/styles/global.css'
import { observer } from 'mobx-react-lite'

export const App = observer(() => {
	return (
		<div className={s.common_wrapper}>
			<MainRoutes />
		</div>
	)
})
