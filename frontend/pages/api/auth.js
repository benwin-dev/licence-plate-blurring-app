import { passport } from '@/api-lib/auth';
import { auths } from '@/api-lib/middlewares';
import { ncOpts } from '@/api-lib/nc';
import nc from 'next-connect';

console.log("API 1");

const handler = nc(ncOpts);

console.log("API Z");

handler.use(...auths);

console.log("API 3");

handler.post(passport.authenticate('local'), (req, res) => {
  console.log("API 4");
  
  res.json({ user: req.user });
});

handler.delete(async (req, res) => {
  await req.session.destroy();
  res.status(204).end();
});

export default handler;
