import s from "./AddTItle.module.scss"

export const AddTItle = () => {
	return (
		<div className={s.main}>
			<div className={s.container}>
				<div className={s.title_wrapper}>
					<div className={s.title}>Creating a title</div>
				</div>

				<div className={s.images_wrapper}>
					<div className={s.images_cover}>
						<div className={s.images_cover_title}>Cover</div>
						<div className={s.images_cover_img}></div>
					</div>
					<div className={s.images_background}>
						<div className={s.images_background_title}>Background</div>
						<div className={s.images_background_img}></div>
					</div>
				</div>

				<div className={s.inputs_wrapper}>
					<input type='text' placeholder='blabla' />
					<input type='text' placeholder='blabla' />
					<input type='text' placeholder='blabla' />
					<input type='text' placeholder='blabla' />
					<input type='text' placeholder='blabla' />
					<input type='text' placeholder='blabla' />
					<input type='text' placeholder='blabla' />
				</div>

				<div className={s.buttons_wrapper}>
					<button className={s.btn_send}>Send</button>
					<button className={s.btn_back}>Back</button>
				</div>
			</div>
		</div>
	)
}
