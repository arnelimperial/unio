import axios from 'axios'
import { jwtDecode } from 'jwt-decode'

const getAccessToken = () => {
  const jwtAtom = localStorage.getItem('jwtAtom')
  let token = jwtAtom ? JSON.parse(jwtAtom) : null
  if (token) return token.access
}

const getRefreshToken = () => {
  const jwtAtom = localStorage.getItem('jwtAtom')
  let token = jwtAtom ? JSON.parse(jwtAtom) : null
  if (token) return token.refresh
}

const http = axios.create({
  headers: {
    Accept: 'application/json',
  },
  timeout: 100000,
})

// Interceptor
http.interceptors.request.use(
  async (config) => {
    const token = getAccessToken()

    let expiresIn = localStorage.getItem('expAtom') || 0

    if (token) {
      config.headers['Authorization'] = 'Bearer ' + `${token}`
    } else if (new Date(expiresIn) <= new Date() && token !== undefined) {
      const _refreshToken = getRefreshToken()

      const reqTokenResponse = await axios.post('/api/refresh', {
        refreshToken: _refreshToken,
      })

      localStorage.setItem('jwtAtom', JSON.stringify(reqTokenResponse.data))

      const _token = getAccessToken()

      const decoded = jwtDecode(_token)

      localStorage.setItem('expAtom', JSON.stringify(Number(decoded.exp)))

      config.headers['Authorization'] = 'Bearer ' + `${_token}`
    } else {
      config.headers['Content-Type'] = 'application/json'
    }

    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

http.interceptors.response.use(
  (res) => res,
  async (err) => {
    const originalRequest = err.config

    if (err.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const _refreshToken = getRefreshToken()

        const tokenResponse = await axios.post('/api/refresh', { refreshToken: _refreshToken })

        localStorage.setItem('jwtAtom', JSON.stringify(tokenResponse.data))

        const token = getAccessToken()

        const decoded = jwtDecode(token)

        localStorage.setItem('expAtom', JSON.stringify(Number(decoded.exp)))

        originalRequest.headers.Authorization = 'Bearer ' + `${token}`
        return http(originalRequest)
      } catch (_err) {
        if (_err.response && _err.response.data) {
          return Promise.reject(_err.response.data)
        }
        return Promise.reject(_err)
      }
    }
  }
)

const signup = async (input) => {
  const { data: response } = await http({
    method: 'POST',
    url: '/api/signup',
    data: input,
  })

  return response
}

const login = async (input) => {
  const { data: response } = await http({
    method: 'POST',
    url: '/api/login',
    data: input,
  })

  return response
}


const loginRequest = async (identifier, password) => {
  const response = await fetch('/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ identifier, password }),
  });

  if (!response.ok) {
    throw new Error('Invalid credentials');
  }

  return response.json();
};



const httpService = {
  signup,
  login,
  http,
  loginRequest
}

export default httpService