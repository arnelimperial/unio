import { atomWithStorage } from 'jotai/utils'

export const jwtAtom = atomWithStorage('jwtAtom', { access: '', refresh: '' })

