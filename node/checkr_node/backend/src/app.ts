import express from 'express';
import { sequelize } from './config/database';
import { config } from 'dotenv';
import errorMiddleware from './middleware/errorMiddleware';

import userRouter from './routes/UserRoutes';
import adverseActionRouter from './routes/AdverseActionRoutes';
import candidateRouter from './routes/CandidateRoutes';
import courtSearchRouter from './routes/CourtSearchRoutes';
import reportRouter from './routes/ReportRouter';

config();

const app = express();
const port = process.env.PORT;
app.use(express.json());

app.use('/api/',userRouter)
app.use('/api/adverse-actions/',adverseActionRouter)
app.use('/api/candidates/',candidateRouter)
app.use('/api/courtsearches/',courtSearchRouter)
app.use('/api/reports/',reportRouter)

app.use(errorMiddleware);

sequelize.sync({ force: true }).then(() => {
  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
});
