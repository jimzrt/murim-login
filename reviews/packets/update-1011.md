<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1011.txt",
      "sha256": "ab9de2d04a7a0bcd088e4f9df5691cdb8553dc12a494f91792234037026ea8b4",
      "bytes": 14031
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7ba0ca0c0b149bc9121a2ad4fa09f502d0bed36d7127d30847bab34671897c88",
      "bytes": 1488
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "516a8b203d28c7930cfab6973246cc4b7ce64aa1171e07d163cf23cb52f7cc20",
      "bytes": 237525
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "151f1abbe410507a8d5ca8f1857c37750631d6d43b1abdd54d4f4a180888cde5",
      "bytes": 1614
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0c8fc5dd4776200d1c31cec930c902a3607b7107dd1e29009eb7adf1db9b69d7",
      "bytes": 623
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "629f090f2148518e4a1354e017c74226663df694951f56539e7dae55d0fc1f93",
      "bytes": 563
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "ee933eb1cf0e6039bd055997846bb217635fc18bb3d7fa6a5202a7fb7f31f11c",
      "bytes": 733
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8a36c21af3e33ce8297d5a41a312212a7b74793dcd26a6bf5d9ca9c9372e2ef2",
      "bytes": 276653
    }
  ],
  "estimated_tokens": 10508
}
-->

# Durable State Update — Chapter 1011

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1011. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1011. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 1011,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1011,
    "continuity_sources": [1011],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Baekma Bang is the largest group in Ningxia and is opening a trade route west toward Xinjiang.",
    "Baekma Bang scouts saw at least a thousand Dark Heaven tents in the western desert, on a route closer to Gansu than Qinghai.",
    "Ma Junggeol’s group followed the force for a day and a half at a distance of one hundred li before returning with its report.",
    "Taekyung stays in Gansu and departs with a force of nearly three thousand toward the threatened front.",
    "Gansu has three defensive lines and about thirty thousand troops; Dunhuang is the foremost line and can be reached by the allied force in three days at full speed.",
    "Ma Junggeol estimates Dark Heaven could reach Gansu in about twenty days, possibly sooner; a worst-case estimate puts the first battle one or two days away.",
    "Some Gansu leaders still suspect Ma Junggeol and his men, who are effectively being held hostage while accompanying the force.",
    "Taekyung’s linked Quest, “Road of Blood,” requires annihilating hostile forces in Gansu; failure means Dark Heaven wins and Gansu’s control is lost."
  ],
  "continuity_sources": [
    1009,
    1010
  ],
  "open_questions": [
    "Who was the unknown master who helped reform the Ningxia bandit leaders?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?"
  ],
  "safe_through": 1010,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마적     | **mounted bandits**                              |                                                       |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 도사      | **Daoist**                                                      |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마중걸 | **Ma Junggeol** |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 진태경 | 마중걸 | Murim Alliance member to visiting horse-caravan chief | Junggeol | casual | Initially addresses him familiarly, then apologizes and shifts to polite speech. |
| 마중걸 | 진태경 | visiting horse-caravan chief to young Murim Alliance member | young man | polite and deferential | Initially calls him a pretty little gigolo as an insult, then uses a respectful address. |
| 마중걸 | 사마공 | visiting group leader to sect leader | Sect Leader Sima | polite and respectful | Addresses him as 사마 문주 while explaining Ningxia and Baekma Bang. |
| 사마공 | 마중걸 | sect leader to visiting group leader | you | formal and probing | Uses 자네 while questioning Ma Junggeol about following Dark Heaven. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1010
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1010
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1010
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** He is initially confrontational under pressure but becomes formal and earnest when explaining his group’s purpose.
- **Voice:** Not established
- **Relationships:** He leads six associates who, with him, are known as the Seven Masters of Baekma Bang.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1010
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1011화



누군가를 의심하는 것은 썩 긍정적인 행동이 아니다.

하지만 지금 같은 전시(戰時) 상황에서의 의심은 곧 신중함이다.

계속해서, 깊게 들여다볼수록 그 실체가 뚜렷해지고 승리를 향해 조금씩 가까워진다.

그리고 그것이 마중걸을 비롯한 백마칠종(白馬七宗)이 일행에 합류하게 된 가장 큰 이유였다.

정확히 말하자면, 내가 이끄는 화룡각에.

‘물론 내가 앞장서서 자처한 거긴 하지만.’

본래는 사마공의 감시하에 놓일 예정이었으나, 내가 적지 않은 병력을 통솔해야 하는 그의 상황을 이야기하자 결론은 금세 나왔다.

화룡각에 배속되는 것으로.

워낙 시간이 촉박했던 탓에 더 이상의 반론은 나오지 않았지만, 나는 똑똑히 보았다.

백마칠종의 처우에 관한 결론이 내려졌던 그 순간, 한층 깊게 가라앉은 사마공의 눈빛을.

‘기분 탓인가. 아니면…….’

내심 말꼬리를 흐린 나는 마중걸을 힐끗 바라보았다.

사람을 앞에 두고 무시한다며 투덜거리던 그는 어느샌가 조용해진 상태였다.

아니, 겉보기에만 그랬다.

두두두!

힘차게 내달리는 말발굽과 그에 따라 전신을 휘감으며 스쳐 지나가는 거센 바람.

그리고…….

우우웅.

그 사이로 은밀하게 전해지는 미세한 파동.

‘이건.’

본능적으로 직감할 수 있었다.

이것은 고절한 경지에 다다른 자만이 느낄 수 있는 기의 흐름이라는 것을.

더불어 크고 작은 여러 소음에 파묻혀 전해져오는 저 미세한 파동 속에는, 지금껏 듣지 못했던 목소리가 담겨 있다는 것을.

스아아아.

그건 이성적인 판단을 통한 계산이 아니었다. 잠시 잊고 있던 본능이었다.

나는 이제야 막 두 발로 설 수 있다는 것을 깨달은 아이처럼, 마중걸을 중심으로 흘러나오는 파동을 향해 기를 흘려보냈다.

닿고, 뒤섞이고, 이내 하나가 되었다.

파동의 주인인 마중걸조차 눈치채지 못할 만큼 자연스럽게.

그리고 그것은, 얼마 떨어지지 않은 위치에서 같은 종류의 파동을 주고받던 그의 여섯 의형제 또한 예외가 아니었다.

- ……제까지 이대로 끌려가야 합니까?

그렇게 미세하던 파동, 아니 전음(傳音)이 비로소 내 귓가에 또렷이 울려 퍼진 그 순간이었다.

띠링.



- 숨겨진 업적, [내 귀에 도청 장치]를 달성하셨습니다!

- 이제부터 주위의 [전음]을 감지하고 엿들을 수 있게 되었습니다!

- 이는 위대한 경지에 도달한 이에게 허락된 또 하나의 공능, 그러나 너무 기뻐하지는 마십시오. 대상과 시전자의 수준에 따라 엿들을 수 있는 [전음]에도 한계가 있으니까요!



‘……이게 되네.’

멍하니 눈을 깜빡이던 것도 잠시, 나는 귓가로 전해지는 전음에 귀를 기울이기 시작했다.

어디, 무슨 작당 모의를 하나 들어나 보자.



* * *



- 나 참, 언제까지 이대로 끌려가야 합니까?

- 맞습니다. 이건 뭐 숫제 인질도 아니고.

- 후, 아버지. 오늘따라 당신이 너무 그립습니다.

- 어? 형님 아버지는 이십 년도 전에 돌아가시지 않았어요?

- 그러니까 더 보고 싶지.

- 아.

불만 가득한 아우들의 전음에, 마중걸은 준엄한 어조로 대꾸했다.

- 어허, 뭘 그리 투덜거리느냐. 애초부터 예상했던 일이거늘.

비상시에는 누구보다 먼저 도망치지만, 평소에는 대형을 하늘처럼 섬기는 둘째 아우가 고개를 끄덕였다.

- 갈! 대형 말씀이 백번 천번 옳으니 모두 그만해라. 처음부터 이런 상황을 예견하지 않으셨다면 우리를 이런 사지(死地)에 끌고 오셨겠느냐?

역시 둘째다.

형보다 나은 아우 없다는 말이 괜히 나왔겠는가.

때맞춰 다른 아우들을 조곤조곤 타이르는 난쟁이의 모습에 마중걸이 흐뭇하게 미소지은 그때였다.

- 아까 대형이 했던 말 못 들었소?

사사건건 다리를 거는 셋째가 불쑥 던진 한마디에, 둘째가 눈을 끔뻑거렸다.

- 아까? 아까 언제?

- 출발 직전에 말이오. 멀쩡한 말안장을 점검한답시고 혼자 멀찍이 떨어져서 쥐똥만 한 목소리로 혼잣말을 하고 있길래 들어 봤더니…….

- 들어 봤더니?

- 아니, 들을 필요 없다. 별거 아니니 신경 쓰지 말아라.

반 시진 전의 일이 생각난 마중걸이 황급히 가로막았지만, 셋째 아우의 전음은 이미 바람을 타고 전해지고 있었다.

- 좆 됐다. 이제 어떡하지. 그러고 있더이다.

- ……!

- ……!

북풍 설한보다 싸늘한 바람이 주위를 휩쓸었다.

순간 내려앉은 무거운 침묵 속, 사정없이 뒤통수를 후벼 파는 여섯 개의 시선에 마중걸의 눈동자가 침잠하게 가라앉았다.

- 대형…….

- 셋째 형님 말이 사실이오?

- 아닐 겁니다. 아니죠? 그렇죠?

- 이게 사실이면 진짜…….

- 가, 갈. 대형께서 그러실 리 없다.

- 뭘 그럴 리가 없어 없기는. 내가 이 귀로 똑똑히 들었다니까.

할 말을 잃은 마중걸은 눈동자만 뒤룩뒤룩 굴렸다.

이걸 어떻게 대답해야 하나.

무심코 흘러나온 혼잣말을, 그것도 하필이면 셋째가 듣고 있었을 줄은 정말 꿈에도 몰랐다.

- 그게, 그러니까…….

계속 침묵할 수도 없어 더듬더듬 흘려보낸 전음.

동시에 눈치 빠른 여섯 아우는 탄식을 내뱉었다.

- 맞네.

- 진짜네.

- 아, 어머니. 오늘따라 미치도록 뵙고 싶습니다.

- 그럴 때가 있죠. 이미 오래전에 돌아가신 분이라 더욱더 사무치게 그리운.

- 미친놈인가. 아직 정정하신 분을 왜 죽여.

- 아.

- 갈……!

- 대형, 그래서 이제 진짜 어쩔 겁니까. 이대로라면 쭉 전선까지 끌려가서 칼받이 되는 거 아니오?

혼돈에 빠진 다른 이들과 달리, 그나마 현실을 직시하고 있는 셋째 아우의 물음에 마중걸은 아주 미세하게 고개를 저었다.

- 걱정할 것 없다. 비록 내가 생각했던 것보다 약간, 아주 조금 더 상황이 좋지 않게 흘러가고는 있지만 셋째의 말처럼 칼받이로 쓰이진 않을 테니.

- 칼받이가 아니면 화살받이로 쓰겠지. 고맙소. 대형 덕분에 우리 전부 인생 종 쳤소.

- 어허, 그럴 일 없대도!

- 아니, 대형은 뭘 믿고 그리 장담하는 게요? 막말로 당장 까라면 까야 하는 게 우리 처지 아니오?

- 그건…….

- 주위를 좀 둘러보시오. 살면서 한번 보기도 어려운 초절정 고수만 벌써 몇 명인지. 저런 괴물들이 등 쿡쿡 찌르면서 눈치라도 주면, 우리 같은 놈들은 뭐 빠지게 달려 나가서 싸워야 하는 거요.

울분을 토해 내는 듯한 셋째 아우의 전음을 시작으로, 다른 의형제들의 토로가 빗발쳤다.

- 우리를 완전 도적놈들 취급하는 종남파 말코 도사들에, 바로 그 흑야왕에, 말로만 듣던 화왕과 반쯤 미친 것 같은 젊은 제자 놈까지 있지.

- 특히 대형 코앞에 있는 저 진태경이라는 놈은 제정신이 아닙니다. 성문 지나기도 전에 삼도천 건널 뻔했던 거 잊었습니까?

- 염병, 이러려고 마적단 때려치웠나. 솔직히 말해서 저희의 과거가 썩 자랑스러운 건 아니지만, 그래도 약탈 한번 해 보기도 전에 때려치우지 않았습니까? 주야장천 칼만 벼리다가 막상 뽑아 보지도 못했구먼.

- 갈! 생각해 보니까 더럽게 억울하네. 우리가 지금껏 약탈을 했어, 무고한 양민들을 죽이길 했어, 이제 좀 마음 잡고 한탕 해 보자 할 때 대인(大人)을 만나 개심한 거 아니오? 좀 착하게 살아 보려고 하는데 진짜 너무하네.

- 둘째 형님 말이 맞소. 우리가 상판이 이렇게 생겨 먹어서 그렇지, 다른 놈들처럼 흉악한 짓거리만 골라서 하고 다녔으면 대인께서 가만히 놔뒀겠냐고. 안 그렇소?

서러움이 한가득 담긴 전음들을 듣고 있자니, 마중걸 역시 자신도 모르게 마음 한구석이 찡하게 울려올 지경이었다.

맞다. 자신들이 뭘 잘못했는가.

물론 전직 마적이었던 것은 부정할 수 없지만, 하늘을 우러러 맹세코 벌 받을 만한 짓은 하지 않았다.

‘그런 짓을 하고 이런 취급을 받았다면 차라리 억울하지나 않지.’

양민을 상대로 약탈?

굳게 마음을 먹어도 막상 쳐들어가면 아무것도 못 했다.

이미 다른 마적단에 의해 싸그리 털린 그들에게서 무엇을 뜯어낼 수 있겠나. 배가 고파 울지도 못하는 갓난아이를 안고 있는 일가족을 위해 되려 식량을 내어준 적도 부기지수였다.

뿐인가.

겉보기에만 흉신악살(凶神惡殺)이지, 마중걸은 포함한 일곱 의형제는 천성부터가 겁이 많았다.

그렇기에 양민을 죽이거나 약탈하는 건 처음부터 무리였고, 간혹 드물게 녕하성으로 상행을 온 배짱 넘치는 상단과 마주치더라도 통행료만 받고 보내줬다.

이유?

간단했다.

‘무서우니까.’

이 흉흉한 세상에 제대로 된 호위 병력도 없이 녕하성 같은 무법지대를 드나들 리가 있나.

어느 표국이나 상단이건 최소 수십의 칼잡이를 대동하는 것이 당연했고, 서로가 대치한 그 팽팽한 분위기 속에서 마중걸은 흉악한 상판을 내밀며 이렇게 말하면 됐다.

‘결국, 피를 볼 셈인가?’

마두 뺨치는 인상과 준엄하기 그지없는 어조가 합쳐지면 훌륭한 대화 수단이 된다.

그 상대가 표국이든, 상단이든, 혹은 살인에 도가 트다 못해 우화등선을 목전에 둔 마적단이든.

당시만 하더라도 무공이 일천했던 마중걸과 여섯 의형제들은 그렇게 하나의 마적단으로 살아남을 수 있었다.

‘대인’이라 불리는 그가 나타나기 전까지.

그리고 자신들을 올바른 길로 이끌어준 대인의 존재를, 마중걸은 지금 이 순간에도 굳게 믿고 있었다.

- 모두 그만!

일순간 마중걸이 힘주어 흘려보낸 전음에, 등 뒤에서 빗발치던 의형제들의 토로가 뚝 끊겼다.

그리고 마중걸은 그 찰나의 빈틈을 놓치지 않았다.

- 아무것도 걱정할 것 없다. 나야 그렇다 치더라도, 설마하니 대인께서 이러한 상황을 염두에 두지 않으셨겠느냐?

- 음.

- 그건 그렇군.

- 대형이면 몰라도 대인이라면 다르긴 하죠.

- 그렇지. 대형은 못 믿어도 대인은 믿지.

- 듣고 보니 그러네.

- 웬일로 맞는 말을 하는구려.

뭔가 곱씹을수록 기분이 묘해지는 답변들이었지만, 마중걸은 떨떠름한 마음으로 전음을 이어갔다.

- 녕하에 소식을 전한다는 빌미로 애들 몇 명 돌려보냈으니 필시 대인께도 이 소식이 전해질 터. 그때까지 경거망동하지 말도록 해라. 알겠느냐?

그때, 셋째인 주먹코가 불쑥 끼어들었다.

- 그런데, 그것도 대인께서 멀쩡하실 때 이야기 아닙니까?

- 뭐?

- 아니, 그렇잖아요. 대형께서도 잘 아시다시피 그분이 워낙에 좀…… 오락가락하시니까.

잠시 눈을 끔뻑거리던 마중걸이 더듬더듬 대답했다.

- 괘, 괜찮을 것이다. 아마도.

그러나 굳이 마중걸의 자신 없는 대답이 아니더라도, 누구도 확신할 수 없는 부분이라는 것은 다른 의형제들 역시 잘 알고 있었다.

- 하, 씨. 셋째 형님 말 듣고 나니까 좀 쎄한데.

- 하지만 최근에는 그나마 멀쩡하시지 않았습니까? 그러니 저희가 앞으로 나아가야 할 방향 같은 것도 이것저것 알려 주셨던 거죠.

- 그랬지. 그랬는데…… 언제 훼까닥할 지 모르는 게 그분 아니냐.

- 대인이야 처음 뵀을 때부터 이상했지. 머리는 온통 봉두난발에, 며칠을 안 씻었는지 얼굴도 새카매서는 완전히 거지꼴이 따로 없었잖소. 심지어 지금도 마찬가지고.

- 이거 큰일인데. 지금 대인께서 오락가락하는 상태라면 애들이 찾아가도 무용지물일 것 아니오?

깊어지는 의형제들이 근심 속, 가뜩이나 못생긴 얼굴을 한껏 찌푸린 채 머리를 굴리던 마중걸이 마침내 입을 열었다.

- 어쩔 수 없군. 우리 중 하나가 직접 가는 것이 좋겠다. 그나마 자주 보던 얼굴들을 마주하신다면 하루라도 빨리 정신을 차리실지 모르니.

- 우리 중 하나라면, 누구?

- 글쎄. 지금부터 정해 봐야지.

- 정한 다음에는, 어떻게 보내려고? 지금 상황에서는 어려울 텐데?

- 그건 대형인 내가 잘 알아서 해결할 일이니까 걱정 말…… 아니 잠깐만.

문득 전음을 멈춘 마중걸이 눈살을 찌푸렸다.

- 그런데 아까부터 영 말이 짧은 게, 혓바닥이 반 토막이라도 났나. 어느 싸가지 없는 놈이냐? 어?

바로 그 순간이었다.

생각지도 못한 누군가의 육성이 마중걸의 귓가를 파고든 것은.

“난데.”

“……?”

“나라고.”

설마. 아니겠지.

내심 중얼거린 마중걸은, 달싹이는 입술을 가리기 위해 살짝 숙이고 있던 고개를 천천히 들었다.

그리고 자신을 향해 살벌하게 웃고 있는, 그 싸가지 없는 놈의 얼굴을 확인할 수 있었다.

“어, 어어.”

귀신에라도 씐 것처럼 부르르 떠는 마중걸을 향해, 진태경이 부드럽게 웃어 보였다.

“나한테 해 줘야 할 얘기가 많은 것 같은데. 안 그래요?”
```

## Final English reading copy

```markdown
# Chapter 1011

There was nothing particularly positive about suspecting someone.

But in a time of war like this, suspicion was just another word for caution.

The more you looked, and the deeper you dug, the clearer the truth became—and the closer you came to victory.

That was the biggest reason Ma Junggeol and the other six masters of Baekma Bang had joined our group.

Or, to be precise, the Fire Dragon Pavilion I led.

*Though I was the one who stepped forward and volunteered.*

They were originally supposed to be placed under Sima Gong’s watch. But when I explained that he had his hands full commanding a sizable force, we reached a decision in no time.

They would be assigned to the Fire Dragon Pavilion.

We were in such a hurry that no one raised any further objections. Still, I saw it clearly.

The moment the decision about the Seven Masters of Baekma Bang was made, Sima Gong’s eyes sank deeper than before.

*Am I imagining it? Or…*

I let the thought trail off and glanced at Ma Junggeol.

He’d been grumbling about how rude it was to ignore someone standing right in front of you, but at some point he’d gone quiet.

Or so it seemed.

*Thud-thud-thud!*

The horses’ hooves thundered as they galloped, and the fierce wind coiled around us and rushed past.

And…

*Wooooong.*

A faint ripple passed stealthily through it all.

*This is…*

I could feel it instinctively.

This was a flow of energy only someone who had reached a profound realm could sense.

And within that faint ripple, carried to me beneath the clamor of countless sounds, was a voice I’d never heard before.

*Ssshhh.*

This wasn’t some calculated conclusion I’d reached through reason. It was an instinct I’d forgotten I had.

Like a child who had only just learned to stand on two feet, I sent my qi toward the ripple emanating from Ma Junggeol.

It touched the ripple, mingled with it, and soon became one.

So naturally that even Ma Junggeol, the ripple’s source, didn’t notice.

Nor did his six sworn brothers, who were exchanging the same kind of ripples with one another not far away.

“…How long do we have to be dragged along like this?”

That was the moment the faint ripple—no, the Sound Transmission—rang clearly in my ears at last.

*Ding.*

> **System**  
> Hidden achievement **A Bug in My Ear** achieved!  
> You can now detect and eavesdrop on nearby **Sound Transmissions**!  
> This is another ability granted to those who reach a great realm. But don’t get too excited. The **Sound Transmissions** you can eavesdrop on are limited by the levels of both the target and the user!

*…So I can do this now.*

I blinked in a daze for a moment, then focused on the Sound Transmissions reaching my ears.

Let’s hear what sort of conspiracy they’re cooking up.

* * *

“Honestly, how long do we have to be dragged along like this?”

“Exactly. What are we, hostages?”

“Whew, Father. I miss you so much today.”

“Huh? Didn’t your father pass away more than twenty years ago?”

“That’s why I miss him even more.”

“Oh.”

At his younger brothers’ grumbling Sound Transmissions, Ma Junggeol answered in a stern voice.

“Now, now. Why are you all complaining so much? We expected this from the start.”

The second brother, who fled faster than anyone in an emergency but worshipped the Chief like the heavens the rest of the time, nodded.

“Enough! The Chief is a hundred, a thousand times right, so all of you shut up. If he hadn’t foreseen a situation like this from the beginning, would he have dragged us into such a deathtrap?”

That was the second brother for you.

There was a reason people said no younger brother could outdo his older brother.

Just then, Ma Junggeol smiled with satisfaction at the sight of the little man gently putting the others in their place.

“Didn’t you hear what the Chief said earlier?”

At the third brother’s abrupt remark—he always had to stick his foot in everything—the second brother blinked.

“Earlier? When?”

“Right before we left. He wandered off on his own, supposedly to check a perfectly good saddle, and muttered something in a tiny voice. I listened, and…”

“You listened, and?”

“No, there’s nothing to hear. It was nothing, so don’t worry about it.”

Remembering what he’d said half a shichen earlier, Ma Junggeol hurriedly tried to cut him off. But the third brother’s Sound Transmission was already riding the wind.

“We’re fucked. What do we do now?”

“……”

“……”

A wind colder than the bitter north wind swept through the group.

In the heavy silence that fell, six pairs of eyes bored mercilessly into the back of Ma Junggeol’s head. His eyes sank darkly.

“Chief…”

“Third Brother, is that true?”

“It’s not, is it? It isn’t, right?”

“If that’s true, then seriously…”

“E-enough! There’s no way the Chief would say that.”

“What do you mean, ‘there’s no way’? I heard it with my own ears.”

At a loss for words, Ma Junggeol’s eyes darted back and forth.

How was he supposed to answer that?

He’d never dreamed the third brother would hear him mutter to himself—especially when he’d let it slip without thinking.

“That, well…”

Unable to stay silent forever, he hesitantly sent his reply.

At once, his six perceptive brothers let out a collective groan.

“So it’s true.”

“It really is.”

“Ah, Mother. I want to see you so badly today.”

“Sometimes it’s like that. You miss them all the more when they passed away so long ago.”

“Are you crazy? She’s still perfectly healthy. Why are you killing her off?”

“Oh.”

“Enough…!”

“Chief, what are we actually going to do now? At this rate, they’ll drag us all the way to the front and use us to catch swords, won’t they?”

Unlike the others, who were caught up in the chaos, the third brother was at least facing reality. Ma Junggeol gave the faintest shake of his head.

“Don’t worry. Things are going a little—just a little—worse than I expected, but they won’t use us to catch swords like you said.”

“If it’s not swords, they’ll use us to catch arrows. Thanks, Chief. You’ve ruined all our lives.”

“Now, now. I said that won’t happen!”

“Then what are you basing that confidence on, Chief? Let’s be blunt. If they tell us to jump, we have to ask how high, don’t we?”

“Well…”

“Take a look around. There are already several Supreme Peak masters here—people you’d be lucky to see once in your life. If those monsters start prodding us in the back and giving us the look, what choice do guys like us have except to sprint out and fight like hell?”

The third brother’s Sound Transmission sounded like an outpouring of pent-up anger. His sworn brothers chimed in one after another.

“There are those Zhongnan Sect Daoist punks treating us like outright bandits, the Black Night King himself, the Fire King, and that young Disciple of his who looks half-mad.”

“Especially that Jin Taekyung standing right in front of the Chief. He’s not right in the head. Have you forgotten how we nearly crossed the Sanzu River[^1] before we’d even made it through the gate?”

“Damn it, is this why we quit being mounted bandits? I’ll admit our past wasn’t exactly something to brag about, but we quit before we’d even gotten to rob anyone! We spent all day, every day sharpening our swords and never even got to draw them.”

“Enough! Now that I think about it, this is downright unfair. Have we robbed anyone? Killed any innocent civilians? We were just about to get our act together and pull off one decent score when we met the Lord and turned over a new leaf. We’re trying to live a little more honestly, and this is just too much.”

“Second Brother’s right. Sure, we look like this, but if we’d gone around doing only the most vicious things like everyone else, do you think the Lord would’ve left us alone? Isn’t that right?”

Listening to their Sound Transmissions, brimming with sorrow, Ma Junggeol felt a pang in his own heart.

They were right. What had they done wrong?

Of course, he couldn’t deny that he used to be a mounted bandit. But he could swear to heaven that they’d never done anything deserving punishment.

*If we’d actually done those things, at least this treatment wouldn’t feel so unfair.*

Robbing civilians?

Even when they steeled themselves and rode out to attack, they couldn’t bring themselves to do a thing.

What could they take from people who’d already been stripped of everything by other mounted-bandit groups? Countless times, they’d even given away their own food to families holding newborns too hungry to cry.

And that wasn’t all.

Although they looked like fiends, Ma Junggeol and his six sworn brothers were timid by nature.

Robbing or killing civilians had been impossible for them from the start. And even when they occasionally came across a gutsy merchant caravan traveling to Ningxia Province, they just collected a toll and let it pass.

Why?

Simple.

*Because they were scared.*

Who would travel through a lawless place like Ningxia Province without a proper escort?

It was only natural for an Escort Bureau or merchant caravan to bring at least several dozen armed men. In that tense standoff, Ma Junggeol just had to put on his vicious face and say:

*“So, you mean to shed blood after all?”*

A fiendish-looking face paired with a stern voice made for an excellent negotiating tactic.

Whether the other party was an Escort Bureau, a merchant caravan, or a mounted-bandit group so practiced at killing that they were nearly ready to ascend to immortality.

Back then, Ma Junggeol and his six sworn brothers knew little about martial arts. That was how Ma Junggeol and his six sworn brothers, whose martial arts were still rudimentary back then, had survived as a mounted-bandit group.

Until the man they called “the Lord” appeared.

And even now, Ma Junggeol firmly believed in the Lord who had led them onto the right path.

“Enough, all of you!”

At Ma Junggeol’s forceful Sound Transmission, the grievances streaming from behind him cut off at once.

He didn’t let that brief opening go to waste.

“There’s nothing to worry about. Even if you don’t trust me, surely you trust that the Lord would have anticipated a situation like this?”

“Hmm.”

“That’s true.”

“If it’s the Lord, that’s different. The Chief, maybe not, but the Lord, yes.”

“Right. We can’t trust the Chief, but we can trust the Lord.”

“Now that you mention it, that makes sense.”

“For once, you’re saying something right.”

The answers only made him feel stranger the longer he thought about them, but Ma Junggeol continued his Sound Transmission with a vague sense of unease.

“I sent a few men back on the pretext of relaying news to Ningxia, so the Lord will surely hear about this. Until then, don’t do anything rash. Understood?”

Just then, the third brother, the one with the bulbous nose, cut in.

“But that’s only if the Lord’s in his right mind.”

“What?”

“Well, isn’t it? You know as well as anyone how he can be a little… all over the place.”

Ma Junggeol blinked a few times, then stammered out a reply.

“H-he’ll be fine. Probably.”

But even without Ma Junggeol’s uncertain answer, his sworn brothers knew it was something no one could be sure about.

“Damn. Now that Third Brother’s said it, I’ve got a bad feeling.”

“But hasn’t the Lord been more or less all right lately? That’s why he’s been telling us this and that about the direction we should head.”

“He has. But with him, you never know when he’ll snap.”

“The Lord was strange from the first time we met him. His hair was a complete mess, and his face was so black he looked like he hadn’t washed in days. He was a regular beggar. He still looks the same now, too.”

“This is bad. If the Lord’s off his rocker right now, sending the men to him will be useless, won’t it?”

As his sworn brothers’ worry deepened, Ma Junggeol scrunched up his already ugly face and thought it over. At last, he spoke.

“We have no choice. One of us should go in person. Maybe seeing some familiar faces he sees often will help him come to his senses sooner.”

“One of us? Who?”

“Hard to say. We’ll have to decide now.”

“Once we decide, how are you going to send him? That’ll be difficult in our current situation.”

“As the Chief, I’ll figure that out, so don’t worry—wait a minute.”

Ma Junggeol abruptly stopped his Sound Transmission and frowned.

“You’ve been getting awful casual with me for a while now. Did you lose half your tongue or something? Which insolent bastard is it? Huh?”

That was the exact moment.

Someone’s actual voice, from someone he hadn’t expected, pierced Ma Junggeol’s ears.

“Me.”

“…?”

“It’s me.”

No. Impossible. Surely not.

Muttering to himself, Ma Junggeol slowly raised his head. He’d been keeping it slightly lowered to hide his moving lips.

And there, facing him, was that insolent bastard, smiling menacingly.

“Uh, uhh.”

Ma Junggeol shuddered as if possessed by a ghost. Jin Taekyung smiled warmly at him.

“Looks like there’s a lot you need to tell me. Isn’t that right?”

[^1]: The Sanzu River is a Buddhist river said to lie between the world of the living and the afterlife.
```
