import s from "./App.module.scss"
import { MainRoutes } from "./pages/MainRoutes/MainRoutes"

function App() {
	return (
		<div className={s.common_wrapper}>
			<MainRoutes />
		</div>
	)
}

export default App
