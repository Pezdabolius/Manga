import { Routes, Route } from "react-router-dom"
import { MainPage } from "../../pages/Main/MainPage"
import { Header } from "../../widgets/Header/Header"
import { MangaItem } from "../../features/MangaItem/MangaItem"
import { MangaCatalog } from "../../pages/CatalogPage/MangaCatalog"

export const MainRoutes = () => {
	return (
		<>
			<Header />
			<Routes>
				<Route path='/catalog' element={<MangaCatalog />} />
				<Route path='/' element={<MainPage />} />
				<Route path='/manga-item/:title' element={<MangaItem />} />
			</Routes>
		</>
	)
}
