import { useEffect, useRef, useState } from 'react'
import s from './Header.module.scss'
import { Link } from 'react-router-dom'
import { observer } from 'mobx-react-lite'

export const Header = observer(() => {
	const [isCatalogOpen, setCatalogOpen] = useState(false)
	const [isCatalogOpen2, setCatalogOpen2] = useState(false)
	const catalogRef = useRef<HTMLLIElement>(null)
	const catalog2Ref = useRef<HTMLLIElement>(null)

	const handleClickOutside = (event: MouseEvent) => {
		if (catalogRef.current && !catalogRef.current.contains(event.target as Node)) {
			setCatalogOpen(false)
		}
		if (catalog2Ref.current && !catalog2Ref.current.contains(event.target as Node)) {
			setCatalogOpen2(false)
		}
	}

	useEffect(() => {
		document.addEventListener('mousedown', handleClickOutside)
		return () => {
			document.removeEventListener('mousedown', handleClickOutside)
		}
	}, [])

	const toggleCatalogMenu = () => {
		setCatalogOpen(!isCatalogOpen)
	}
	const toggleCatalogMenu2 = () => {
		setCatalogOpen2(!isCatalogOpen2)
	}

	return (
		<header className={s.header}>
			<nav className={s.nav}>
				<Link to='/' className={s.nav_brand}>
					MangaApp
				</Link>
				<div className={s.nav_menu}>
					<ul className={s.menu_list}>
						<li ref={catalogRef} onClick={toggleCatalogMenu} className={s.menu_item}>
							catalog
							{isCatalogOpen && (
								<div className={s.dropdown_catalog}>
									<ul>
										<li>manga</li>
										<li>comic</li>
									</ul>
								</div>
							)}
						</li>
						<li className={s.menu_item}>search</li>
						<li className={s.menu_item}>discussion</li>
						<li ref={catalog2Ref} onClick={toggleCatalogMenu2} className={s.menu_item}>
							...
							{isCatalogOpen2 && (
								<div className={s.dropdown_add_author}>
									<ul>
										<Link to='/'>
											<li>Add Author</li>
										</Link>
										<Link to='/'>
											<li>Add Artist</li>
										</Link>
										<Link to='/'>
											<li>Create Team</li>
										</Link>
									</ul>
								</div>
							)}
						</li>
					</ul>
				</div>
				<div className={s.nav_menu2}>
					<ul>
						<li className={s.nav_sign_in}>sign in</li>
						<li className={s.nav_sign_up}>sign up</li>
						<li className={s.nav_color_theme}>theme</li>
					</ul>
				</div>
			</nav>
		</header>
	)
})
