import s from "./App.module.scss"
import { MainRoutes } from "./layouts/MainRoutes/MainRoutes"
import "./assets/styles/reset.css"

function App() {
	return (
		<div className={s.common_wrapper}>
			<MainRoutes />
		</div>
	)
}

export default App
