import { Routes, Route } from "react-router-dom"
import { MainPage } from "../../pages/Main/MainPage"
import { Header } from "../../widgets/Header/Header"

export const MainRoutes = () => {
	return (
		<div>
			<Header />
			<Routes>
				<Route path='/' element={<MainPage />} />
			</Routes>
		</div>
	)
}
