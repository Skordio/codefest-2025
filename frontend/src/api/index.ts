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
      return response.data;
    } catch (error) {
      console.error('API GET error:', error);
      throw error;
    }
  }

  // Example: Post data to Flask backend
  async post(endpoint: string, data: any) {
    try {
      const response = await this.api.post(endpoint, data);
      return response.data;
    } catch (error) {
      console.error('API POST error:', error);
      throw error;
    }
  }
}

// Create an instance with Flask backend URL
const api = new ApiService('http://localhost:5000');

export default api;
