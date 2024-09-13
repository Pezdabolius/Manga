import { Routes, Route } from "react-router-dom"
import { Home } from "../home/Home"
import { Header } from "../../components/header/Header"
import { AddAuthor } from "../managementMangaInfo/addAuthor/AddAuthor"
import { AddArtist } from "../managementMangaInfo/addArtist/AddArtist"
import { CreateTeam } from "../managementMangaInfo/createTeam/CreateTeam"

export const MainRoutes = () => {
	return (
		<div>
			<Header />
			<Routes>
				<Route path='/' element={<Home />} />
				<Route path='/add-author' element={<AddAuthor />} />
				<Route path='/add-artist' element={<AddArtist />} />
				<Route path='/create-team' element={<CreateTeam />} />
			</Routes>
		</div>
	)
}
