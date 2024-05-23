import express from 'express';
import router from './routes';
import sequelize from './database';
import errorMiddleware from './middleware/errorMiddleware';

const app = express();
const PORT = process.env.PORT;

app.use(express.json());

app.use('/api', router);
app.use(errorMiddleware);

sequelize.sync().then(() => {
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
});