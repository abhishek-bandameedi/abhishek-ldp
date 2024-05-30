import { z } from "zod";

export const signUpSchema = z.object({
  email: z.string().email({ message: "Enter a valid email" }),
  password: z
    .string()
    .min(8, { message: "Please enter a password with at least 8 characters" })
    .regex(/^[a-zA-Z0-9]+$/, { message: "Password must be alphanumeric" }),
});

export const loginSchema = z.object({
  email: z.string().email({ message: "Email is incorrect" }),
  password: z.string().min(8, { message: "Password is incorrect" }),
});

export const createCandidateSchema = z.object({
  candidate_name: z
    .string()
    .min(3, { message: "Name must be at least 3 characters long" }),
  candidate_email: z.string().email({ message: "Enter a valid email" }),
  dob: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  zipcode: z.string().regex(/^\d+$/, { message: "Zipcode must be numeric" }),
  phone_no: z
    .string()
    .regex(/^\d+$/, { message: "Phone number must be numeric" }),
  location: z.string(),
  social_security_no: z.string(),
  driver_liscence: z.string(),
  created_at: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  userId: z.number(),
});

export const createReportSchema = z.object({
  status: z.enum(["clear", "consider", "schedule"]),
  adjudication: z.enum(["-", "adverse-action", "engage"]),
  package: z.string(),
  created_At: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  completed_at: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  candidateId: z.number().int().positive(),
});

export const updateAdjudicationSchema = z.object({
  adjudication: z.enum(["-", "adverse-action", "engage"]),
});

export type UpdateAdjudicationSchemaType = z.infer<
  typeof updateAdjudicationSchema
>;

export const createCourtSearchSchema = z.object({
  search: z.string(),
  status: z.string(),
  date: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  candidateId: z.number().int().positive(),
});

export const createAdverseActionSchema = z.object({
  status: z.string(),
  pre_notice_date: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  post_notice_date: z.string().refine((date) => !isNaN(Date.parse(date)), {
    message: "Enter a valid date",
  }),
  candidateId: z.number().int().positive(),
});

export type signUpSchemaType = z.infer<typeof signUpSchema>;

export type loginSchemaType = z.infer<typeof loginSchema>;

export type CreateCandidateSchemaType = z.infer<typeof createCandidateSchema>;

export type CreateReportSchemaType = z.infer<typeof createReportSchema>;

export type CreateCourtSearchSchemaType = z.infer<
  typeof createCourtSearchSchema
>;

export type CreateAdverseActionSchemaType = z.infer<
  typeof createAdverseActionSchema
>;
