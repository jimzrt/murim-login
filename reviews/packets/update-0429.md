<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0429.txt",
      "sha256": "9d692ff6086b6e92e26b0c93b2f84b23ea759a6399c63ee290f60261a8f74d77",
      "bytes": 15033
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0cbaff8970818c26e5852b3d641e6b66141abe4ff5f6bb3f71202c31b74132c5",
      "bytes": 1723
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "873e8683007b06e0696ed16200a88f88414899189bcfbd59c4aae3baa2be719f",
      "bytes": 141887
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "854405901e26a30d64261a15c49c93409870de78918848ce68caaa5417f141ed",
      "bytes": 533
    },
    {
      "path": "characters/Felix.md",
      "sha256": "9fe2f2a247b37021cea41751b4b992cf29f0c0eec76d749bad86ecad53d07a48",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "24cb30af9ad628df0aa0a0aae878da53fd39fdc257853da569e7185e1bbe16e3",
      "bytes": 1286
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "957ef47ae0607011036dd7cbe75c55676854e98a1471f4b26ada7585c1f3bbe3",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "6e0710a2752294586e3c538884ef68d869006469eda320a127e2b99efcb2ea55",
      "bytes": 893
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "aff88ad5ca86ab0689b0e0dbfbaf3c7fefb7f5f491397333c487d1e301b9f226",
      "bytes": 132017
    }
  ],
  "estimated_tokens": 10715
}
-->

# Durable State Update — Chapter 429

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 429. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 429. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 429,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 429,
    "continuity_sources": [429],
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
    "Jin Taekyung has regained consciousness and is active after the Arch Lich's defeat, though his recovery was publicly announced after a delay.",
    "Jin's improved internal-energy control lets him manipulate modern medical devices powered by Magic Gems.",
    "Chairman Shao Yang is preparing a political reckoning against the Crown Prince Party after enduring persecution and forced labor under the faction.",
    "Lee Jungryong is publicly presumed dead without a surviving body, and Wu Heixing's corpse was recovered after the battle.",
    "Jin's mother and Hayeon are in China under Chairman Shao's protection and have confronted Jin over his secret departure.",
    "Jin publicly attributes Wu Heixing's death to the Arch Lich and claims Wu's potion saved him.",
    "Jin publicly mourned Lee Jungryong and the other war dead, and the press conference drew approximately three billion live viewers.",
    "Jin went to find an unidentified person after the press conference."
  ],
  "continuity_sources": [
    428
  ],
  "open_questions": [
    "Who is the unidentified person Jin went to find after the press conference, and why?",
    "What final punishment will be imposed on Wu Heixing's father and the Crown Prince Party leadership?"
  ],
  "safe_through": 428,
  "temporary_decisions": [
    "Render 최 팀장 as “Team Leader Choi” and 종석 할아버지 as “Grandpa Jongseok.”",
    "Render 샤오 주석 as “Chairman Shao” and 샤오 양 주석 as “Chairman Shao Yang.”",
    "Retain “jajinmori” for 자진모리장단 with a brief explanatory footnote.",
    "Preserve Jin's profane, dry, and deliberately misleading public voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 대주     | **Squad Leader** / **Commander**             |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 사천     | **Sichuan**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 평화 | **Peace Guild** | Guild name. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 427
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 427
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 428
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton King is his friend and ally.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 428
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 426
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

## Korean source

```text
＃429화



「바로 그쪽으로 이동할까요?」

기자 회견이 끝나자마자 다가온 임시 경호팀장, 아니 샤오 쉔의 물음에 나는 고개를 끄덕였다.

“그러자. 어디 계신지는 알지?”

「예, 알고 있습니다. 그럼 가시죠.」

샤오 쉔을 위시한 수십 명의 경호원이 나를 둥글게 에워싸고 천천히 이동하기 시작했다.

그러자 동시에 주위에서 일대 혼란이 일어났다. 카메라와 마이크를 든 방송국 놈들이 우르르 몰려온 것이다.

「미스터 진! 필릭스 왕자 전하와 친분이 있다는 게 사실입니까!」

「진 상! 진 상!」

네가 진상이다, 인마.

기자 회견으로도 만족하지 못한 각국의 기자들이 달라붙었지만, 헌터로 이루어진 경호원들을 뚫을 수 없었다.

아, 기어코 다가와 끈질기게 마이크를 들이미는 인간도 있긴 했다.

“진태경 씨! 같은 한국인인데 인터뷰 한 번만…….”

어딜 가나 꼭 이런 사람들이 있기 마련이지.

“아, 예. 같은 한국인인데 좀 비켜 주세요.”

대충 대답해 주고 지나치려던 나는 문득 어디선가 본 얼굴에 멈칫했다. 그러곤 기자를 막아서려는 샤오 쉔을 제지하며 물었다.

“잠깐만. 혹시 다스패치 소속이세요?”

“……!”

“맞는 것 같은데. 제 기사 올렸었죠?”

“아, 아닌데요.”

맞네. 저 시벌 놈.

어디서 봤나 했더니 내가 모태 솔로라는 기사를 특종이랍시고 인터넷에 올렸던 그 기자다. 그 이후로 포털 사이트에 내 이름을 치면 관련 검색어로 진태경 모쏠이 뜨더라.

“쉔아.”

한국어로 나누는 대화를 알아듣지 못해 어리둥절하던 샤오 쉔이 고개를 숙였다.

「예, 형님.」

“탄압해라.”

「넵.」

씩씩하게 대답한 샤오 쉔이 다스패치 기자의 손목을 붙잡았다.

「선생님, 균형을 집행하겠습니다.」

“잠, 잠깐만!”

이미 늦었다. 어마어마한 힘에 붕 떠오른 기자가 사람들 사이로 떨어졌다. 몇 개의 카메라가 부서지고 각국의 언어로 욕설이 우박처럼 쏟아진다.

오대양 육대주를 아우르는 쌍욕의 향연에 나는 감탄사를 내뱉었다.

“여기가 지구촌이로구나.”

「네?」

“아냐. 계속 가자.”

때마침 대기하고 있던 공안들까지 달려와 합세하자 길이 뚫렸다.

나는 사람들의 시선과 빈틈없는 호위 아래 목적지로 향했고, 잠시 후 VVIP들이 머무르고 있는 5성급 호텔의 스위트 룸에서 그를 만날 수 있었다.

“존슨.”

「오, 진. 생각보다 일찍 왔네?」

심각한 얼굴로 뭔가를 들여다보고 있던 매직 존슨이 환하게 웃으며 자리에서 일어났다.

두꺼운 손으로 내 어깨를 두드린 그가 나를 자리로 안내하며 물었다.

「그래. 기자 회견은 잘 끝났고?」

묻는 걸 보니 기자 회견을 직접 보진 않은 모양이다. 나는 존슨이 건네는 캔맥주를 받아 들며 대답했다.

“그냥저냥. 질문에 적당히 대답해 주고 30분 만에 끝냈죠, 뭐.”

「하하. 기자들이 별로 안 좋아했겠는데.」

“존슨보다는 절 훨씬 좋아할걸요? 전 그나마 기자 회견이라도 했으니까.”

매직 존슨은 전쟁이 끝나자마자 곧장 숙소에 틀어박혀 모습을 보이지 않았다.

또 다른 S급 헌터인 파이 첸이나 필릭스 왕자와 달리 어디에도 모습을 드러내지 않았으니, 일각에선 그의 사망설이 흘러나올 정도였다.

그 지경까지 가고 나서야 본인의 SNS 공식 계정에 짤막한 코멘트를 하나 남긴 것이 그가 보인 행보의 전부였다.



새로운 것을 연구하고 있다.

이것은 이번에 거둔 승리처럼 신비롭고 위대하다.



아마 대부분의 사람들은 저게 정확히 무슨 뜻인지 몰라 고개만 끄덕이고 넘어갔겠지만, 나는 그가 말한 ‘새로운 것’의 정체를 아는 몇 안 되는 사람이다.

“그래서, 어떻게 됐습니까?”

매직 존슨이 입가를 움찔거리며 대답했다.

「글쎄.」

“오, 성공적으로 끝난 모양이네요.”

「난 아무 말도 안 했는데?」

“웃음 참는 거 티 엄청 나요.”

「아닌데? 전혀 아닌데?」

아니긴 뭐가 아니야.

기대감에 가득 찬 그의 눈빛에 나는 피식 실소를 흘렸다.

“처음에는 싫어하셨다던데.”

「넌 그때 찾아오지도 않았잖아. 최가 그렇게 말했어?」

“또 누가 있겠어요. 현재로서는 저랑 존슨, 최 팀장님까지 단 세 명만 알고 있는 비밀인데.”

「이런. 하지만 최가 전한 말 중에 틀린 게 있어.」

“틀린 거?”

「응. 난 처음부터 거절하지 않았거든.」

500ml짜리 캔맥주를 한입에 털어 넣은 매직 존슨이 심각한 어조로 말을 이었다.

「마법을 날리려고 했지.」

“아하.”

「농담 아냐. 그때 네가 내 입장이었다고 생각해 봐. 아마 객실을 산산조각으로 만들었을걸?」

“저였으면 호텔을 부쉈죠.”

하지만 객실도, 호텔도 멀쩡할 수 있었던 건 매직 존슨이 ‘대마도사’였기 때문이다.

인간은 호기심의 동물이라고도 불리지만, 마법사는 호기심 그 자체다. 그 정점에 선 대마도사야 말할 것도 없었다.

그리고 지금껏 보지 못한 ‘새로운 것’에 대한 제안을, 그는 흔쾌히 받아들였다.

「최의 설명을 듣고, 직접 보면서도 믿을 수 없었지. 이건 정말이지…….」

몽롱한 눈동자로 중얼거리던 매직 존슨이 돌연 고개를 저었다.

「아니지. 이럴 게 아니라 직접 확인해 봐.」

“잘됐네요. 기다리다가 늙어 죽을 뻔했는데.”

반쯤 남은 캔맥주를 내려놓고 일어난 나는, 망설임 없이 걸어가 넓은 스위트 룸 어딘가에서 발걸음을 멈췄다.

“여기죠?”

매직 존슨이 고개를 끄덕였다. 기운의 흐름에 민감한 S급 헌터가 이상함을 알아차리는 건 그리 놀라운 일이 아니다.

「맞아. 역시 잘 아네.」

“이 정도면 정말 어지간해서는 모르겠네요.”

겉보기에는 그저 공간의 한 부분일 뿐이다. 그러나 나는 이미 룸에 발을 디딘 순간부터 알고 있었다.

이것이 모든 소리와 광경을 차단한 마법이라는 것을.

「잠깐 기다려 봐. 내가 바로 마법을 해제할…….」

후웅, 서걱!

매직 존슨은 말을 잇지 못하고 눈을 크게 떴다.

강기에 휩싸인 내 손날이 허공을 내리그음과 동시에, 그가 펼쳐 놓은 각종 마법이 깨끗하게 갈라졌기 때문이었다.

「진. 이게 도대체……?」

아크 리치와의 싸움 도중 중단전을 개방한 덕분에 기의 결을 볼 수 있게 되었다.

그 후부터 ‘이런 일’이 가능하게 되었지만, 나는 별다른 설명을 덧붙이지 않고 정면을 응시했다.

마법의 해제와 더불어 한 꺼풀 벗겨지는 공간. 그 너머에 한 사람이 우뚝 서 있었다.

“아, 에, 이, 오, 우. 안넝하세오. 판캅습니다. 쿡밥충 조아요. 기움치 싸랑해요.”

전신 거울 앞에서 뭔가를 들고 어색한 발음으로 한국어를 연습하던 금발의 외국인이 거울에 비친 내 모습을 발견하고 돌아선다.

기생 오래비 같은 얼굴에 언뜻 웃음이 스쳤다.

“드디어 왔구나, 간악한 인간.”

이 새끼 이런 것만 정확히 발음하는 것 보소.

아주 잠깐, 한 대 때려 줄까 고민하던 나는 이내 실소를 흘리며 입을 열었다.

“못 본 사이에 잘생겨졌다?”

금발의 외국인, 스켈레톤 킹이 득의양양한 목소리로 대답했다.

“넌 못 본 사이에 더 못생겨졌군.”

“…….”

“존못.”

“……아니, 시벌 놈이.”

이 자식 한국어 도대체 어디에서 배운 거야.



* * *



「음. 역시 아름답군. 전혀 이질감이 없어.」

매직 존슨은 강남 성형외과 의사처럼 연신 흡족하게 웃었다.

「다시 봐도 희대의 역작이야. 스켈레톤의 뼈. 그것도 완전히 새로운 네임드 몬스터의 뼈에 마법진을 새긴 마법사는 인류 역사상 내가 최초일걸?」

집도의의 자화자찬이 아니라, 정말 사실이 그랬다.

윤기가 흐르는 금발에 신비롭게 빛나는 금안(金眼). 190센티에 이르는 체격은 균형이 잡혀 있고 길쭉한 팔다리에는 적당한 체모까지 나 있다.

그뿐인가. 선명한 근육과 핏줄, 호흡이나 침을 삼킬 때마다 보이는 몸의 반응까지.

나조차도 정말 자세히 주의를 기울여야 이상함을 알아차릴 만큼, 스켈레톤 킹은 완전한 인간의 모습을 하고 있었다.

“……와, 이게 되네.”

밑져야 본전이라는 생각으로 부탁한 거였는데, 이 정도로 완벽할 줄이야.

놀라움에 침을 꿀꺽 삼킨 내가 녀석의 금발을 만져 보려 손을 뻗은 그때였다.

스윽.

한 걸음 물러난 스켈레톤 킹이 오만한 눈빛으로 나를 바라보았다.

“더러운 손 치워라. 머릿결 상한다.”

“…….”

“탈모 걸리면 책임질 건가?”

이 새끼 인간 다 됐네…….

어이가 없으려니까 말도 안 나온다. 순간 말문이 막힌 나를 무시한 스켈레톤 킹이 전신 거울에 비친 자신의 모습을 보며 만족스럽게 웃었다.

“음. 대존잘.”

“……아까부터 궁금했던 건데, 너 그런 말은 어디서 배웠냐?”

“인터넷에서.”

“인터넷?”

“그렇다. 일주일 동안 오지고 지리게 봤지.”

“너 설마 폰도 있냐?”

“저기 있는 고마운 인간이 하나 사 줬다. 땡큐, 존슨.”

통역 마법을 사용 중인 매직 존슨이 흐뭇한 미소와 함께 고개를 끄덕였다.

「성공적인 새 출발을 기원하네. 미스터 킹.」

“땡큐, 존슨.”

땡큐 존슨 같은 소리 하네. 영어 기본 회화는 또 언제 배운 거야.

나는 매직 존슨에게 즉각 따져 물었다.

“아니, 폰까지 사 줬어요?”

「헤이, 진. 뭐가 문제야? 내 막내딸은 다섯 살인데 그 아이도 스마트폰을 써.」

“그건 존슨의 막내딸 얘기고, 쟤는 스켈레톤 킹이잖아요.”

“잠깐. 간악한 인간이여. 대화 도중에 미안하지만, 이 말은 반드시 해야겠군.”

정색하며 끼어든 스켈레톤 킹이 말을 이었다.

“앞으로는 스톤-킹이라고 부르거라.”

“이건 또 뭔 돌팔매질 당할 소리야.”

“이 몸의 새로운 이름이다. 스톤 킹. 미국 조지아주 애틀랜타에서 출생한…….”

나는 두통을 느끼며 중얼거렸다.

“죽여 버릴까, 확 그냥.”

“미국 시민을 죽일 셈인가?”

“누가 미국 시민이야, 미친놈아.”

“지금 당장은 아니더라도 곧 미국 국적을 취득할 수 있다.”

“차라리 카카오페이지에 웹소설을 써라. 어떤 놈이 그런 개소리를 해?”

매직 존슨이 수줍게 팔을 들어 올렸다.

「진, 내 연줄이면 충분히 가능…….」

“아! 아악! 아아아악!”

미치고 팔짝 뛰겠다.

나는 지끈거리는 이마를 붙잡고 매직 존슨에게 말을 건넸다.

“저기, 존슨.”

「음?」

“제가 최 팀장님을 통해 부탁했던 건, 그냥 사람처럼 보이게끔만 만들어 달라는 거였는데요.”

「아, 물론 그랬지. 저 친구가 간절히 원했다며?」

이 모든 일은 내가 처음 깨어난 직후, 스켈레톤 킹의 강력한 주장에 의해 벌어졌다.

자신이 언제까지 답답한 인벤토리에 갇혀 있어야 하냐며 불만을 터트린 것이다.

전투에서 큰 공을 세운 것을 참작하여 그만한 보상을 달라는 것이 놈의 주장이었고, 나와 최 팀장의 입장에서는 충분히 합당한 요구였다.

‘레이페이와의 전투에서 최 팀장과 샤오 쉔을 지키기도 했고, 녀석 덕분에 아크 리치를 쓰러트릴 수 있었지.’

안 그래도 스켈레톤 킹에 관한 보답을 해야겠다고 생각하던 찰나였다.

그뿐만 아니라 녀석이 인간의 형태를 갖추게 된다면 여러모로 편한 점이 많았다.

더 이상 모습을 숨기지 않아도 되고, 평화 길드와 계약하여 상부상조할 수도 있으니까.

그런데…….

“일단 제가 말씀드렸던 동양인의 모습이 아니잖아요. 아무리 국내에 외국인들이 많아졌다고 해도 한국에서는 눈에 띈다고요. 특히 이런 외모는.”

매직 존슨이 뭐라 대답하기도 전에, 스켈레톤 킹이 굳은 목소리로 끼어들었다.

“내가 바꿔 달라고 했다.”

“뭐? 왜?”

“인터넷에서 봤다. 잘생긴 백인 남성은 전 세계 어디에서나 통하더군.”

“……통하면 어쩔 건데.”

“나도 연애를 하고 싶다.”

“오, 신이시여.”

깊이 한탄하는 내 어깨를 매직 존슨이 두드렸다.

「괜찮아, 진.」

“괜찮긴 뭐가 괜찮아요. 요즘 세상에 SNS가 얼마나 무서운데. 네티즌들이 신상 털었는데 미국 조지아주 애틀랜타 출생이 아니라 마계 토박이라고 해 봐요. 말이나 됩니까? 도대체 존슨은 왜 저런 부탁을 들어주신 거예요?”

「내 취향의 얼굴을 한번 만들어 보고 싶었어.」

“예?”

「저 얼굴이 내 이상형이야.」

아니, 시발…….

순간 할 말을 잃은 내게, 마지막 인내심을 끊는 한마디가 들려왔다.

“억울한가. 존못.”

“야, 이 개새끼야!”

빡!

순식간에 몸을 튕겨 놈의 정수리에 주먹을 꽂았다.

컥, 하는 신음과 함께 혀를 깨물었는지 스켈레톤 킹의 입가에서 붉은 피가 솟구친다.

붉은 피라니. 이것도 환상 마법인가. 구현 진짜 잘했……이 아니라.

“죽어! 죽어!”

“컥! 커헉!”

건장한 떡대 둘이 뒹굴기 시작하자 룸 안이 난장판이 되는 건 순식간이었다.

그리고 그 여파에 휩쓸린 책상이 우지끈 무너지고 매직 존슨이 들여다보고 있던 서류 뭉치가 내 얼굴 위로 와르르 쏟아졌다.

“자, 잠깐! 간악한 인간이여! 눈앞이 안 보인다!”

“넌 오늘 버릇을 고쳐놔……!”

그리고 다음 순간, 나는 움직임을 우뚝 멈췄다.

눈앞을 가린 종이 뭉치들 사이로 보이는, 기이하면서도 낯익은 어떤 문양들 때문이었다.

‘이건…….’

스켈레톤 킹을 내버려 두고 자리에서 일어난 나는, 멍하니 문양이 프린트된 종이를 집어 들었다.

‘사천.’

틀림없다.

쓰촨이 아니라 사천에서 봤던 바로 그 문양이었다.
```

## Final English reading copy

```markdown
# Chapter 429

“Should we head there right away?”

The acting Head of Security—no, Xiao Shen—approached me as soon as the press conference ended and asked the question. I nodded.

“Let’s do that. You know where he is, right?”

“Yes, I do. Then let’s go.”

Dozens of security personnel led by Xiao Shen formed a circle around me and began moving slowly.

At the same time, chaos erupted all around us. Reporters from various networks, cameras and microphones in hand, came rushing over in a swarm.

“Mr. Jin! Is it true that you’re close to His Highness Prince Felix?”

“Jin-san! Jin-san!”[^1]

*You’re the real jinsang here, asshole.*

[^1]: The Japanese address “Jin-san” sounds like the Korean word *jinsang*, meaning an obnoxious nuisance.

The reporters from various countries hadn’t been satisfied with the press conference and latched onto me, but they couldn’t break through the Hunter security detail.

Of course, there was always someone who managed to push his way closer and stubbornly shove a microphone in my face.

“Mr. Jin Taekyung! We’re both Korean, so just one interview…”

There were people like this wherever you went.

“Oh, sure. We’re both Korean, so please move aside.”

I gave him a halfhearted answer and was about to walk past when I suddenly stopped. His face looked familiar.

I stopped Xiao Shen as he moved to block the reporter and asked,

“Wait a second. Are you with Daspatch?”

“……!”

“I thought so. You published an article about me, didn’t you?”

“Oh, no, I didn’t.”

*That confirms it. You son of a bitch.*

I’d been wondering where I had seen him before. He was the reporter who had posted an article about me having been single my entire life and called it an exclusive.

After that, whenever I typed my name into a search portal, “Jin Taekyung single since birth” showed up as a related search term.

“Shen.”

Xiao Shen, who hadn’t understood our Korean conversation and was looking bewildered, lowered his head.

“Yes, hyung.”

“Crack down on him.”

“Yes, sir.”

Xiao Shen answered energetically and grabbed the Daspatch reporter by the wrist.

“Sir, I will enforce balance.”

“W-Wait a second!”

It was already too late. The reporter was lifted into the air by tremendous force and dropped into the crowd.

Several cameras broke, and curses in languages from around the world poured down like hail.

I let out an exclamation of admiration at the feast of profanity spanning five oceans and six continents.

“So this is the global village.”

“Huh?”

“Never mind. Let’s keep going.”

The public-security officers who had been waiting nearby arrived and joined us, clearing a path.

Under the eyes of the crowd and the protection of an impenetrable escort, I headed toward my destination.

A short while later, I met him in the suite of the five-star hotel where the VVIPs were staying.

“Johnson.”

“Oh, Jin. You got here earlier than I expected.”

Magic Johnson, who had been staring at something with a serious expression, smiled brightly and rose from his seat.

He patted my shoulder with his thick hand, guided me to a seat, and asked,

“So, did the press conference go well?”

Judging by the question, he probably hadn’t watched the press conference himself.

I accepted the canned beer Johnson handed me and answered,

“It was all right. I gave reasonable answers to their questions and wrapped it up in thirty minutes.”

“Ha-ha. I doubt the reporters were very happy.”

“They’ll like me much more than they like you. At least I held a press conference.”

As soon as the war ended, Magic Johnson had shut himself away in his accommodations and refused to show himself.

Unlike Faye Chen or Prince Felix, the other S-rank Hunters, he hadn’t appeared anywhere. Some people had even begun spreading rumors that he was dead.

Only after things had reached that point did he leave a brief comment on his official social-media account. That was the full extent of his public activity.

> I am researching something new.
>
> It is as mysterious and magnificent as the victory we achieved this time.

Most people had probably nodded and moved on without knowing what that meant.

But I was one of the few people who knew the identity of the “new thing” he was talking about.

“So? How did it turn out?”

Magic Johnson answered, the corners of his mouth twitching.

“Who knows?”

“Oh, then I guess it ended successfully.”

“I didn’t say anything.”

“You’re doing a terrible job of hiding that you’re holding back a laugh.”

“I’m not. Not at all.”

*Of course you are.*

At the sight of his eyes shining with anticipation, I let out a quiet laugh.

“I heard you didn’t like it at first.”

“You didn’t come to see me then. Did Choi tell you that?”

“Who else could have told me? At the moment, this secret is known by only three people: me, Johnson, and Team Leader Choi.”

“Ah. But there was one mistake in what Choi told you.”

“A mistake?”

“Yes. I didn’t refuse from the beginning.”

Magic Johnson downed the contents of his five-hundred-milliliter can of beer in one gulp, then continued in a grave tone.

“I was about to fire off a spell.”

“Oh.”

“I’m not joking. Imagine that you were in my position. You probably would have smashed the entire suite to pieces.”

“If I’d been you, I would’ve destroyed the hotel.”

The suite and the hotel had survived only because Magic Johnson was a Grand Mage.

Humans were sometimes called animals of curiosity, but mages were curiosity itself. A Grand Mage at the very pinnacle of magic was no exception.

And when he received an offer involving a “new thing” he had never seen before, he accepted it readily.

“After hearing Choi’s explanation and seeing it with my own eyes, I still couldn’t believe it. This is truly…”

Magic Johnson mumbled with hazy eyes, then suddenly shook his head.

“No. This won’t do. Come and see for yourself.”

“Good. I nearly grew old and died waiting.”

I set down the half-empty can of beer and stood. Without hesitation, I walked across the spacious suite and stopped somewhere inside it.

“This is the place, right?”

Magic Johnson nodded. It wasn’t particularly surprising that an S-rank Hunter sensitive to the flow of energy would notice something strange.

“That’s right. You’re very perceptive.”

“Even someone fairly observant would have a hard time noticing this.”

At a glance, it was nothing more than a section of the room.

But I had known from the moment I stepped into the suite.

*This is magic that blocks out every sound and sight.*

“Wait a moment. I’ll dispel the magic right aw—”

Whoosh. Slash!

Magic Johnson couldn’t finish his sentence. His eyes widened.

The edge of my hand, wrapped in Force, swept down through empty air, and the various spells he had laid out split apart cleanly.

“Jin. What on earth…?”

During my battle with the Arch Lich, I had opened my Middle Dantian and gained the ability to see the texture of qi.

From then on, I had become capable of doing things like this. But I didn’t bother offering an explanation and simply stared straight ahead.

As the magic was dispelled, a single layer peeled away from the space before me.

Beyond it stood a single person.

“Ah, eh, ee, oh, oo. Hellow. Nishe to meet you. I like rice-soup freaks. I wuv kimchi.”

A blond foreigner had been practicing Korean in front of a full-length mirror while holding something in his hands. When he noticed my reflection in the mirror, he turned around.

A hint of laughter crossed his pretty-boy face.

“At last, you have arrived, vile human.”

*Look at this bastard pronouncing only that perfectly.*

I briefly considered hitting him, but soon let out a quiet laugh and opened my mouth.

“You’ve gotten better-looking since the last time I saw you.”

The blond foreigner, the Skeleton King, answered in a smug voice.

“You have become even uglier since the last time I saw you.”

“…….”

“Ugly as hell.”

“……No, you son of a bitch.”

Where on earth had this bastard learned Korean?

* * *

“Hmm. It really is beautiful. There’s no sense of incongruity at all.”

Magic Johnson kept smiling with satisfaction, like a plastic surgeon in Gangnam.

“Even after seeing it again, it’s an unprecedented masterpiece. I might be the first mage in human history to carve a magic circle into the bones of a Skeleton—and not just any Skeleton, but the bones of a completely new Named Monster.”

This wasn’t a surgeon bragging about his own work. It was simply the truth.

Shiny blond hair. Mysteriously glowing golden eyes. A body nearly 190 centimeters tall, with well-balanced proportions and long limbs covered in just the right amount of body hair.

And that wasn’t all.

The clearly defined muscles and veins. The reactions of his body whenever he breathed or swallowed.

Even I had to pay close attention to notice anything strange. The Skeleton King had taken on the complete appearance of a human being.

“……Wow. This actually works.”

I had asked him to do it thinking that, at worst, I had nothing to lose.

I hadn’t expected it to be this perfect.

I swallowed hard in amazement and reached out to touch his blond hair.

That was when it happened.

Swish.

The Skeleton King took one step back and looked at me arrogantly.

“Take your filthy hand away. You will damage my hair.”

“…….”

“If I go bald, will you take responsibility?”

*This bastard is practically human now…*

I was so dumbfounded that I couldn’t even speak.

Ignoring me as I stood there speechless, the Skeleton King looked at his reflection in the full-length mirror and smiled with satisfaction.

“Hmm. Insanely handsome.”

“I’ve been wondering this for a while, but where did you learn expressions like that?”

“On the Internet.”

“The Internet?”

“Indeed. I spent a whole week browsing the shit out of it.”

“Wait. Do you have a phone, too?”

“That kind human over there bought one for me. Thank you, Johnson.”

Magic Johnson was using a translation spell. He nodded with a pleased smile.

“I wish you a successful new beginning, Mr. King.”

“Thank you, Johnson.”

*“Thank you, Johnson,” my ass. When did he learn basic English, too?*

I immediately turned to Magic Johnson.

“Wait. You bought him a phone, too?”

“Hey, Jin. What’s the problem? My youngest daughter is five years old, and even she uses a smartphone.”

“That’s your youngest daughter. He’s the Skeleton King.”

“Hold on. Vile human, I apologize for interrupting your conversation, but I must say this.”

The Skeleton King cut in with a serious expression and continued,

“From now on, call me Stone-King.”

“What fresh hell is this supposed to be?”

“That is my new name. Stone King. Born in Atlanta, Georgia, United States…”

I muttered as I felt a headache coming on.

“Should I just kill him? I’m seriously about to.”

“Would you kill a citizen of the United States?”

“Who’s an American citizen, you lunatic?”

“Perhaps not right now, but I can soon obtain United States citizenship.”

“You should write a web novel for KakaoPage instead. What kind of idiot comes up with that bullshit?”

Magic Johnson shyly raised his hand.

“Jin, with my connections, it should be entirely poss—”

“Ah! Aah! Aaaaah!”

This was driving me insane.

I clutched my throbbing forehead and spoke to Magic Johnson.

“Johnson.”

“Hmm?”

“What I asked Team Leader Choi to do was simply make him look like a human being.”

“Ah, of course. That was what you asked. But I heard this friend desperately wanted it.”

All of this had begun shortly after I first regained consciousness.

The Skeleton King had loudly complained about how long he was supposed to remain trapped inside that cramped Inventory.

His argument was that, in consideration of the great contribution he had made during the battle, he deserved an appropriate reward. From my perspective and Team Leader Choi’s, it was a perfectly reasonable demand.

*He protected Team Leader Choi and Xiao Shen during the battle with Lei Fei, and we managed to defeat the Arch Lich thanks to him.*

I had already been thinking that I needed to reward the Skeleton King.

And if he could take human form, it would be convenient in many ways.

He wouldn’t need to hide anymore, and he could sign a contract with the Peace Guild so that they could help each other.

But…

“For one thing, he doesn’t look like the East Asian appearance I asked for. No matter how many foreigners there are in Korea these days, he’s going to stand out. Especially with a face like that.”

Before Magic Johnson could answer, the Skeleton King cut in with a stiff voice.

“I asked him to change it.”

“What? Why?”

“I saw it on the Internet. Handsome white men do well everywhere in the world.”

“……And what are you going to do with that?”

“I wish to date.”

“Oh, God.”

As I let out a deep sigh, Magic Johnson patted my shoulder.

“It’s all right, Jin.”

“What do you mean, it’s all right? Do you have any idea how terrifying social media is these days? What if netizens dig up his identity and discover that he wasn’t born in Atlanta, Georgia, United States, but is actually a native of the Demon Realm? Does that make any sense? Why did you agree to a request like that?”

“I wanted to try making a face that suited my tastes.”

“What?”

“That face is my ideal type.”

*Oh, for fuck’s sake…*

I had just lost my words when the final blow to my patience arrived.

“Do you feel wronged? Ugly as hell.”

“You son of a bitch!”

Crack!

I launched myself forward and buried my fist in the crown of his head.

The Skeleton King let out a strangled groan. He must have bitten his tongue, because bright red blood spurted from the corner of his mouth.

*Red blood? Was this an illusion spell? He really did a great job of implementing—*

No, that wasn’t the point.

“Die! Die!”

“Ghk! Guhk!”

As two heavily built men began rolling around, the suite was transformed into a disaster zone in an instant.

The desk was caught in the aftermath and collapsed with a splintering crack. The stack of papers Magic Johnson had been examining came cascading down onto my face.

“W-Wait! Vile human! I cannot see!”

“I’m going to teach you some manners today…!”

And then, in the next moment, I stopped moving.

There were strange yet familiar symbols visible among the sheets of paper blocking my view.

*This is…*

I left the Skeleton King where he was and rose from my seat, dazedly picking up a sheet of paper printed with the symbols.

*Sichuan.*

There was no mistake.

It was the exact same pattern I had seen in Sichuan—not the province in China, but Sichuan in Murim.
```
