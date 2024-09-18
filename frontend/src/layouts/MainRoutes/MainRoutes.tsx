import { Routes, Route } from "react-router-dom"
import { MainPage } from "../../pages/Main/MainPage"
import { Header } from "../../widgets/Header/Header"
import { MangaItem } from "../../pages/Main/components/MangaItem/MangaItem"

export const MainRoutes = () => {
	return (
		<>
			<Header />
			<Routes>
				<Route path='/' element={<MainPage />} />
				<Route path='/manga-item/:title' element={<MangaItem />} />
			</Routes>
		</>
	)
}
