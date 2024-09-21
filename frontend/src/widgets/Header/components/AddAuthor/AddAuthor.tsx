import s from "./AddAuthor.module.scss"

export const AddAuthor = () => {
	return (
		<div className={s.main}>
			<div className={s.container}>
				<div className={s.title_wrapper}>
					<div className={s.title}>Add an author</div>
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
