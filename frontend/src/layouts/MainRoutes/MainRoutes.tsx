import { Routes, Route } from "react-router-dom"
import { MainPage } from "../../pages/Main/MainPage"
import { Header } from "../../widgets/Header/Header"
import { MangaItem } from "../../features/MangaItem/MangaItem"
import { MangaCatalog } from "../../pages/CatalogPage/MangaCatalog"
import { AddTItle } from "../../widgets/Header/components/AddTItle/AddTItle"
import { AddAuthor } from "../../widgets/Header/components/AddAuthor/AddAuthor"
import { AddArtist } from "../../widgets/Header/components/AddArtist/AddArtist"
import { AddPublisher } from "../../widgets/Header/components/AddPublisher/AddPublisher"

export const MainRoutes = () => {
	return (
		<>
			<Header />
			<Routes>
				<Route path='/' element={<MainPage />} />
				<Route path='/catalog' element={<MangaCatalog />} />
				<Route path='/manga-item/:title' element={<MangaItem />} />
				<Route path='/add-title' element={<AddTItle />} />
				<Route path='/add-author' element={<AddAuthor />} />
				<Route path='/add-artist' element={<AddArtist />} />
				<Route path='/add-publisher' element={<AddPublisher />} />
			</Routes>
		</>
	)
}
