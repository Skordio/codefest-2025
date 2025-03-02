import axios from 'axios';
import type { AxiosInstance, AxiosResponse } from 'axios';

class ApiService {
  private api: AxiosInstance;

  constructor(baseURL: string) {
    this.api = axios.create({
      baseURL,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  // Example: Fetch data from Flask backend
  async get(endpoint: string) {
    try {
      const response = await this.api.get(endpoint);
      return response;
    } catch (error) {
      console.error('API GET error:', error);
      throw error;
    }
  }

  // Example: Post data to Flask backend
  async post(endpoint: string, data: any, headers?: any) {
    try {
      const response = await this.api.post(endpoint, data, headers);
      return response;
    } catch (error) {
      console.error('API POST error:', error);
      throw error;
    }
  }
}

const publicBackend = 'http://165.227.252.124:5000';
const localBackend = 'http://localhost:5000';

// Create an instance with Flask backend URL
const api = new ApiService(publicBackend);

export default api;
