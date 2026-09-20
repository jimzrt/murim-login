<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0561.txt",
      "sha256": "6a9f74ff709770361db95d22fba0292d24bbe477a23e3eca6fff36c1efc9a99e",
      "bytes": 13172
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4c0ab48685a406428a507ee90572a0c70ef0b3c15200ee94285d7205e45ee209",
      "bytes": 4603
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7512d64a28ecab9c5fe97c4eab72e1e5421609aa78c4227a27ca3858992de20e",
      "bytes": 177925
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "0d1c98307645955de4ea5ce0f980407d8c8320bea1d9490f25299487bdc5aead",
      "bytes": 2367
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b69b8b79b6bf1cb598d8caa3e25d036f41ba8536acf56ec6c4e289053ed0a4b7",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6e037ebe65752c167033c5adde58a61aaf59f4879fe377cb933dfada99558081",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d92ef884de8a3984c4160922377b62ea023dae95e2de7465fba0e734cf789088",
      "bytes": 1182
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "07e4c0a3da61bb684948f8bf6ecae40d2d5ca6e195fdceebf3e2c363a8a20386",
      "bytes": 939
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "53001d2217dbb359b71b407b38d2f1130420c023f3ec398a80b7dbe5b53efc96",
      "bytes": 171745
    }
  ],
  "estimated_tokens": 11081
}
-->

# Durable State Update — Chapter 561

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 561. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 561. Profile updates may replace only one
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
  "chapter": 561,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 561,
    "continuity_sources": [561],
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
    "Magic Johnson’s information records at least thirty-two Mutated Gates in the United States during one week, and the true number is likely higher.",
    "The Peace Guild has risen as the only apparent counterweight to Ares Guild; Team Leader Choi is gathering political, business, and Guild allies to strengthen Peace and weaken Ares.",
    "Magic Johnson and the Wizard Guild will support Team Leader Choi, and Magic has taken Choi by Teleportation to meet influential contacts including Joseph Biden.",
    "Team Leader Choi has confirmed that his blood descends from Cheon Taemin, whose legacy gives him exceptional political and social leverage.",
    "The Fire Dragon Pavilion’s six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion’s first mission to Nanman, and the Peace Guild’s modern-world patronage.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Taekyung knows the actual deaths were caused by him, while Go Jun remains Ares Guild’s Vice Guild Master and regards Taekyung and Choi Minwoo as enemies."
  ],
  "continuity_sources": [
    560,
    559
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "How many additional Gate disasters are being concealed, and what is driving the accelerating Mutated Gate and Monster Wave outbreaks in Korea and abroad?"
  ],
  "safe_through": 560,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can’t Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant’s Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, and 펠릭스 왕자 as Prince Felix."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 창기     | **Spear Energy**                                 | Explicit system skill for Taekyung                    |
| 지부장    | **Branch Leader**                            |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 청해     | **Qinghai**            |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 오크 | **Orc** | Monster species. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 시부럴좌 | **Lord Sibu-leol** | Online nickname derived from Taekyung's public profanity. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 560
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild; attacked by three Black Hunters following a solo drinking outing, with both arms severed below the elbows; his wounds were treated with high-ranking healer recovery magic and advanced potions, his arms were reattached, and he regained consciousness after three days; he has chosen to continue as a Hunter and remain with the Peace Guild after recovering; after beginning the Jin Family’s Cultivation Technique, he completed a complete circulation and learned to perform the Small Circulation independently on the first day, adapting unexpectedly quickly; repeated circulation is expected to improve his physical foundations, and resolving his trauma may allow an early return to Guild work
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 559
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 559
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 560
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 558
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

## Korean source

```text
＃561화



우우웅.

갑자기 진동이 울린 스마트폰. 빠르게 화면을 내용을 확인한 나와 임꺽정, 마지막으로 스켈레톤 킹이 차례대로 입을 열었다.

“이건.”

“태, 태경아!”

“오오. 오오오. 이것 봐라. 미개한 인간들이여. 걸그룹 멤버가 이 몸에게 DM을 보냈느니라.”

“…….”

“…….”

저 시벌놈이 진짜. SNS 작작 하라니까.

‘어쩐지 왜 단톡방에도 없는 새끼 폰이 울리나 했네.’

마음 같아서는 환영 마법이 박살 날 때까지 밟아 주고 싶지만, 지금은 그게 중요한 것이 아니었다.

‘어디 걸그룹 멤버……가 아니라. 또 이런 일이 터지다니.’

가까스로 마음의 소리를 삼킨 나는 스마트폰 화면을 응시했다.

나와 최 팀장을 비롯한 평화 길드 초창기 멤버가 모인 단톡방. 그곳에는 송송이가 다급하게 올린 정보가 올라와 있었다.



〈 평화 길드



송송이

야야야ㅑ

C급 게이트 이상 현상 발생.

지금 막 정부 핫라인 통해서 연락 옴.

마력 수치 폭등 중이래.

시ㅂ라; 왜 안 읽어.

읽었으면 대답을 해. 미친놈아.

김 집사님

미안. 합니다. 지금 청와대에 와 있습니다.

송송이

조ㅣ송합니다;; 김 집사님인줄 몰랐어요;;; 일 보세요......

김 집사님

네. 송이 씨도 행복한 하루^^

송송이

어. 한 명 빼고 다 읽었는데?

읽었으면 누구든 최대한 빨리 가서 알아봐요.

난 거리도 거리인데 처리해야 할 일이 있어서 당장은 못 갈 듯.

[지도 첨부]

?

아 근데 확인해 보니까 저기 게이트가 좀……

일단 가 봐요.

특히 진태경은 읽었으면 바로 답장해라.



‘위치?’

도대체 무슨 게이트길래 저런 반응일까.

의문을 뒤로하고 단톡방에 확인했다는 갑장을 남긴 나는, 첨부된 지도를 확인하자마자 송송이가 왜 그런 반응을 보였는지 즉각 깨달을 수 있었다.

“아, 흠.”

확실히 위치가 좀, 거시기 하긴 하다.

한 박자 늦게 지도를 확인한 임꺽정 역시 얼굴을 굳혔다.

“태경아. 여기 혹시…….”

“아마 생각하시는 그곳이 맞을걸요.”

지도에 찍힌 C급 게이트는 부천에서도 역세권에 속한 노른자위 땅인 데다, 소위 헌터들이 말하는 ‘운빨’을 제대로 받는 곳이었다.

여타의 C급 게이트보다 비교적 상대하기 쉬운 몬스터가 출현하며 마정석도 잘 떨구는 그런 곳.

부천에서만 십 년을 넘게 헌터 생활을 한 임꺽정이나, 내가 모를 수 없는 게이트다.

이곳을 소유한 길드의 이름 역시도.

“이건 별로 반갑지 않은데…….”

낮은 목소리로 중얼거리는 임꺽정의 모습에, 열심히 스마트폰을 만지작거리던 스켈레톤 킹이 고개를 들었다.

“인간들이여. 어디길래 그렇게 유난을 떠는 것이냐?”

내가 조용히 대꾸했다.

“장소가 문제가 아니라, 주인이 문제지.”

“응? 주인?”

“그래.”

게이트는 사적 소유가 불가능하지만, 중견 길드부터는 장기 임대라는 이름으로 게이트의 사실상의 주인 행세를 하고 있다.

그리고 이 주소가 가리키는 C급 게이트를 소유한 길드는 대한민국, 아니 전 세계를 통틀어 모르는 사람이 없다.

“그래서 주인이 누군데?”

스켈레톤 킹의 물음에, 임꺽정이 짤막한 대답을 툭 던졌다.

“아레스 길드.”

순간, 나도 모르게 시선이 그의 양팔을 향했다.

누군가의 명령에 의해 잘려 나간 팔은 언제 그랬냐는 듯 멀끔하게 붙어 있었지만, 옛 고통을 떠올린 듯 희미하게 떨리고 있었다.

“꺽정 아저씨. 아니, 형님.”

“……괜찮아.”

공허한 대답이다.

점점 커지는 몸의 떨림과 어두운 표정이 바로 그 증거였다.

깊게 가라앉은 내 눈빛을 의식한 듯, 그가 애써 인상을 폈다.

“정말 괜찮다니까. 그보다 어서 가 봐라. 마력 수치가 폭등했으면 또 변이 게이트가 발생할지도 모르는데.”

“……아닙니다. 그놈들이 알아서 잘 하겠죠.”

제가 어떻게 갑니까. 이 상황에서. 심지어 다른 누구도 아닌, 그놈들을 도우러.

못 박힌 듯 제자리에서 움직이지 않는 내게, 임꺽정이 희미한 웃음을 지어 보였다.

“태경아.”

“네?”

“괜찮다고 한 거. 그거 빈말 아니다. 그때 내 팔 자른 놈들은 이정룡까지 포함해서 모두 죗값을 치렀고, 재활 훈련도 거의 끝난 거나 다름없어. 요새는 안사람이랑 시간도 보내면서 애들 커 가는 거 보는 게 참 행복하더라.”

“형…….”

“정말 괜찮으니까, 어서 가 봐. 아레스 길드에도 분명히 좋은 사람들이 많을 텐데. 고작 이런 사적인 이유로 돕지 않는다면 두고두고 후회할 거다. 내가 아는 너는 그런 사람이야.”

“……!”

“마음 같아서는 나도 돕고 싶은데, 그건 안 되겠다. 재활이 안 끝난 것도 있지만 기본적으로 실력이 후달려.”

나는 억지 농담과 함께 껄껄 웃는 임꺽정을 가만히 응시하다가, 이내 고개를 끄덕였다.

그의 말이 맞다. 지금 게이트 내부에서 위험과 맞서고 있는 자들은 나와 평화 길드의 적이 아니다.

어떤 위험을 감지했고, 그 위험에서 누군가를 구할 만한 힘이 있다면 나서는 것이 옳았다.

‘그러기 위해 만든 구조팀이니까.’

어쩌면 시스템을 얻은 그 순간부터, 내가 해야 할 일은 정해져 있는 것이었는지도 모르겠다.

나는 임꺽정을 향해 가벼운 눈인사를 건넸다.

“금방 다녀올게요.”

“그래, 다치지 말고.”

“빨리 해치우고 와라. 간악한 인간이여. 그럼 상으로 이 걸그룹 멤버의 셀카를 보여 주지.”

나는 훈훈한 미소를 지으며 스켈레톤 킹에게 말을 건넸다.

“넌 지랄 말고 빨리 따라와. 아니면 벌로 스마트폰을 박살 낼 테니까.”

“……알았다.”

진작 이렇게 나왔어야지. 뒤질라고.



* * *



송송이가 보낸 지도가 가리키는 C급 게이트 [오크의 황무지]에 도착했을 때, 그곳은 이미 다급한 목소리와 고함으로 가득했다.

“마, 마력 수치가 평소보다 두 배 이상 상승했습니다!”

“그건 나도 알아. 그보다 지원 요청은?”

“아, 아직이라고 합니다!”

“이런 씨발, 부천 지부에 사람 남을 거 아냐! 지금 상황이 급하니까 A급 헌터 하나라도 끼워서 보내 달라고 재요청해!”

“그, 그건 이미 전달했는데 부천에 배치된 A급 헌터는 대부분 해외 파견 중이고, 일부는 휴가라서 거절한다고…….”

“뭐? 휴가? 휴가라서 거절을 해? 이런 개……!”

순식간이었다. 분노가 실린 주먹이 주차되어 있던 자동차를 강타한 것은.

콰앙!

굉음과 함께 1억을 호가하는 외제차가 으스러지며 크고 작은 파편이 곳곳으로 튄다.

붉게 달아오른 씨근덕거리던 B급 헌터가 나와 스켈레톤 킹을 발견한 것은 바로 그때였다.

“허, 돌겠네. 이것들이 아무리 급해도 그렇지. 인원 통제 똑바로 안 하…….”

길게 늘어지는 말꼬리의 뒤에, 부릅뜬 눈동자가 따라붙는다.

“어? 어어? 어어어어?”

입술 사이로 끝없이 흘러나오는 물음표와 내 얼굴에 고정된 시선. 코웃음을 친 스켈레톤 킹이 의미심장한 표정으로 입을 열었다.

“후후. 그래, 이 인간이 바로 그 인간이다.”

“……?”

나도 가만히 있는데 왜 이놈이 나서서 지랄일까.

찝찝한 눈빛으로 스켈레톤 킹을 바라본 나는 헛기침을 내뱉었다.

어느새 바쁘게 돌아다니던 이들이 얼어붙은 채로 이쪽을 바라보고 있었기 때문이었다.

“크흠. 혹시 모르시는 분들이 있을까 봐 말씀드리…….”

“진태경!”

“시벌좌!”

“시부럴좌!”

“……려고 했는데. 그럴 필요는 없겠네요.”

하긴. 내 입으로 말하긴 뭣 하지만, 이제 헌터 중에 내 얼굴을 모르는 사람이 있다면 몬스터가 아닌가 의심해 봐야 한다.

“지, 진짜로 그 진태경?”

“가, 가짜로 그 진태경은 아닐걸요.”

“아, 그 뜻이 아니고…….”

“괜찮습니다. 지금 그게 중요한 것도 아니고.”

나는 자동차를 박살 낸 B급 헌터를 향해 물었다.

“잠깐 본 바에 의하면 이쪽 책임자 같으신데. 맞으세요?”

“마, 맞습니다. 저는 아레스 길드 역곡 지부장인 곽한구라고 합니다.”

부천 지부장도 아니고, 그 아래에 있는 수십 명의 하위 지부장 중 하나가 B급 헌터라.

새삼 아레스 길드의 인재풀과 규모가 느껴진다. 잠시 간과했던 사실 한 가지도 함께.

‘표면상 이미지가 있어서 그런가, 생각보다 분위기가 썩 나쁘진 않네.’

아레스 길드와 나는, 그리고 우리 평화 길드는 악연으로 점철되어 있다.

그러나 그건 결국 수면 아래에서 벌어진 싸움. 이런 사실을 모르는 이들의 눈에 비친 수면 위는 평온하고 잔잔하다.

아니, 오히려 지금 아레스 길드원들의 눈빛에는 기대감과 호의까지 비치고 있었다.

‘어쩌면…… 최 팀장이 예상했던 것보다 빠르게 힘을 키울 수 있겠어.’

하지만 지금은 그보다 중요한 일이 기다리고 있는 상황.

문득 뇌리를 스치는 한 줄기 생각을 구석으로 밀어낸 나는, 지부장을 향해 입을 열었다.

“곁다리 다 자르고, 빠르게 본론부터 갑시다.”

“예, 예?”

“지금 길드 지원 어렵죠? 아레스 길드야 뭐, 담당하는 게이트가 한두 개도 아니고. 해외까지 인력 돌리니까.”

“예?”

“지금 사람을 보내도, 도착하면 늦어요. 휴가 중이라는 A급 헌터 새끼는 지금 폰이랑 호출기 꺼 놓고 놀고 있을 거고. 여기 있는 사람들로는 섣불리 진입했다가 구조는커녕 개죽음당할 확률이 높고. 맞죠?”

“그, 그건 모르는…….”

“모르긴 이 사람아. 모르는 건 당장 저 안의 사람들이 얼마나 버티냐는 거고.”

“헉.”

“처음 마력 수치 상승했을 때부터 지금까지 15분 됐습니다. 당장 저 안에서 팀원들이 죽어 가고 있을지도 몰라요.”

“자, 잠시만요.”

가까스로 내 말을 막아선 B급 헌터가 떨리는 목소리로 말을 이었다.

“압니다. 저도 안다고요. 그런데…… 외부인 개입은 길드 방침을 심각하게 위반하는 겁니다.”

“그래서요?”

“저나 다른 팀원들도 당장 진태경 씨께 부탁드리고 싶은 심정입니다. 하지만 그럴 수가 없어요. 이미 들어서 알고 계시잖습니까.”

안다. 헌터로 활동하는 사람이라면 모를 리 없다. 아레스 길드의 규칙이 얼마나 엄격하고 까다로운지.

이정룡은 각 등급의 실력자들만을 선별해서 높고 거대한 우리 안에 가두었다. 아레스 길드에서 축출당한 헌터를 어떤 길드에서도 받아 주지 않는다는 것은, 막연한 도시 괴담이 아니다.

“하.”

“이런 시발…….”

한숨과 욕이 곳곳에서 흘러나온다. 그런 아레스 길드원들을 빤히 바라보던 나는 불쑥 입을 열었다.

“한 명? 아니면 두 명?”

“예? 지금 무슨…….”

“왠지 지금까지 망설이는 사이에 두 명은 죽었을 것 같아서요.”

“지, 진태경 씨!”

“거기 측정하는 아저씨. 지금 마력 수치 몇이에요?”

내 등장에도 측정 장치 앞에서 손톱을 잘근잘근 씹던 C급 헌터 하나가 비명처럼 외쳤다.

“세 배! 평균 마력의 세 배 돌파했습니다!”

“……!”

그 말의 의미를 모르는 사람은, 이 자리에 아무도 없었다.

‘변이 게이트.’

새해가 밝은 지 일주일만에 터진 세 번째 변이 게이트.

작게 혀를 찬 나는 지부장을 똑바로 응시했다.

“뭐 해. 안 열고.”

“……!”

“담당자 동의 없이 들어가는 건 불법이라 안 하려고 했는데, 사람을 살려야 할 거 아냐. 안 그래? 그러니까 그냥 내가 지랄발광을 떨면서 난입한 걸로 하고, 당장 열어.”

질끈 감은 눈. 꽉 쥔 주먹이 파르르 떨린다. 침묵하는 지부장을 뒤로하고 돌아선 그때, 뒤에서 떨리는 목소리가 흘러나왔다.

“내가…… 동의한 걸로 합시다.”

병신인 줄 알았는데, 이 정도면 얼간이 정도는 된다.

실소를 흘린 나는 한마디를 남기고 게이트를 향해 성큼 걸음을 내디뎠다.

“잘리면 연락해요. 평화 길드는 받아 줄 테니까.”
```

## Final English reading copy

```markdown
# Chapter 561

*Brrrrrrr.*

A smartphone suddenly began vibrating. I, Im Kkeokjeong, and finally the Skeleton King checked the screen in rapid succession before opening our mouths one after another.

“What’s this?”

“T-Taekyung!”

“Oh. Ohoho. Look at this, you uncivilized humans. A girl-group member has sent this body a DM.”

“…”

“…”

*That fucking bastard, seriously. I told him to stop screwing around on social media.*

*No wonder the phone of some bastard who isn’t even in the group chat was ringing.*

I felt like stomping him until his illusion magic shattered, but that wasn’t important right now.

*Which girl-group member… No. That’s not it. Another incident like this?*

I barely swallowed my thoughts and stared at the smartphone screen.

It was the group chat for the early members of the Peace Guild, including Team Leader Choi and me. Song Song had urgently posted some information there.



> **Peace Guild**
>
> **Song Song**
>
> Hey hey heyyy
>
> C-rank Gate anomaly.
>
> Just got contacted through the government hotline.
>
> They say the mana levels are skyrocketing.
>
> Shit; why aren’t you reading this?
>
> If you read it, answer me, you crazy bastard.
>
> **Butler Kim**
>
> Sorry. I am at the Blue House right now.
>
> **Song Song**
>
> S-sorry;; I didn’t know it was you, Butler Kim;;; Go take care of your business……
>
> **Butler Kim**
>
> Yes. You have a happy day too, Song-i. ^^
>
> **Song Song**
>
> Huh. Everyone but one person has read it?
>
> Whoever has read this, get over there and check it out as quickly as possible.
>
> It’s far away, and I have things to deal with, so I probably can’t go right away.
>
> **[Map attached]**
>
> ?
>
> Ah, but now that I look at it, that Gate is kind of…
>
> Just go check it out.
>
> Especially you, Jin Taekyung. Reply as soon as you read this.

*Where is it?*

What kind of Gate could make her react like that?

I put my questions aside, left a reply saying I had seen the message, and checked the attached map. The moment I did, I understood why Song Song had reacted that way.

“Ah. Hmm.”

The location was definitely a little… awkward.

Im Kkeokjeong checked the map a beat later, and his expression hardened as well.

“Taekyung. Is this place, by any chance…”

“It’s probably exactly where you think it is.”

The C-rank Gate marked on the map was in a prime location near a subway station in Bucheon. It was also one of those places that benefited from the so-called “luck” Hunters talked about.

The monsters that appeared there were relatively easy to deal with compared to those in other C-rank Gates, and Magic Gems dropped frequently.

There was no way either Im Kkeokjeong, who had worked as a Hunter in Bucheon for over ten years, or I could fail to know this Gate.

The same went for the Guild that owned it.

“This isn’t exactly welcome news…”

At Im Kkeokjeong’s low mutter, the Skeleton King looked up from the smartphone he had been busily fiddling with.

“Humans. Where is this place that you are making such a fuss over?”

I answered quietly.

“The location isn’t the problem. The owner is.”

“Hm? The owner?”

“That’s right.”

Gates could not be privately owned, but starting with the mid-sized Guilds, Guilds acted as their de facto owners under the name of long-term leases.

And there wasn’t a person in Korea—or anywhere else in the world—who didn’t know the Guild that owned the C-rank Gate indicated by this address.

“Then who is the owner?”

At the Skeleton King’s question, Im Kkeokjeong tossed out a short answer.

“Ares Guild.”

For a moment, my gaze shifted involuntarily to his arms.

The arms that had been severed at someone’s command were attached cleanly, as though nothing had ever happened. But they were trembling faintly, as if he had recalled the pain of that day.

“Kkeokjeong Uncle. No—hyung.”

“…I’m fine.”

It was an empty answer.

The tremors running through his body were growing stronger, and his dark expression was proof enough.

As if he had noticed my deeply lowered gaze, he forced his expression to relax.

“I said I’m really fine. More importantly, hurry up and go. If the mana levels have skyrocketed, another Mutated Gate could appear.”

“…No. They’ll handle it themselves.”

*How can I go in this situation? And not to help anyone else, but those bastards.*

I stood rooted to the spot, unable to move. Im Kkeokjeong gave me a faint smile.

“Taekyung.”

“Yes?”

“When I said I was fine, I wasn’t just saying it. The people who cut off my arms, including Lee Jungryong, all paid for their crimes. My rehabilitation training is practically finished, too. These days, I’m happy just spending time with my wife and watching the kids grow up.”

“Hyung…”

“I’m really fine, so hurry up and go. There must be plenty of good people in Ares Guild, too. If you let a petty personal reason stop you from helping, you’ll regret it for a long time. At least, the Taekyung I know would.”

“…!”

“I’d like to help, too, but I can’t. My rehabilitation isn’t finished, for one thing, and more importantly, I’m just not strong enough.”

I quietly watched Im Kkeokjeong laugh heartily alongside that forced joke. Then I nodded.

He was right. The people facing danger inside the Gate were not enemies of me or the Peace Guild.

If I sensed danger and possessed the strength to save someone from it, then stepping forward was the right thing to do.

*That’s what we created the rescue team for.*

Maybe the moment I obtained the System, what I had to do had already been decided.

I gave Im Kkeokjeong a brief look of acknowledgment.

“I’ll be back soon.”

“All right. Don’t get hurt.”

“Deal with it quickly and return. As a reward, I shall show you a selfie of this girl-group member.”

I smiled warmly and spoke to the Skeleton King.

“Quit screwing around and follow me. Otherwise, I’ll smash your smartphone as punishment.”

“…Understood.”

*I should’ve done this from the start. You trying to get yourself killed?*



* * *



When we arrived at the C-rank Gate *Orc Wasteland*, indicated by the map Song Song had sent, the area was already filled with panicked voices and shouting.

“The mana levels have risen to more than twice their normal level!”

“I know that. What about the support request?”

“They say it hasn’t come through yet!”

“Goddammit, there have to be people left at the Bucheon branch! Tell them to send at least one A-rank Hunter and request it again!”

“We already passed that along, but most of the A-rank Hunters stationed in Bucheon are deployed overseas, and some of the others are on vacation, so they’re refusing…”

“What? Vacation? They’re refusing because they’re on vacation? You fucking—!”

It happened in an instant.

A fist filled with rage slammed into a parked car.

*Bam!*

With a thunderous crash, the foreign car worth more than a hundred million won crumpled, sending large and small fragments flying in every direction.

That was when the red-faced, wheezing B-rank Hunter spotted the Skeleton King and me.

“Hell, this is driving me crazy. No matter how urgent things are, they should still be controlling access properly—”

His voice trailed off, followed by a pair of bulging eyes.

“Huh? Uh? Huh? Huhhhhh?”

Question after question spilled from his lips, his gaze fixed on my face. The Skeleton King snorted and opened his mouth with a meaningful expression.

“Heh heh. Yes, this human is that very human.”

“…?”

*Why is this bastard stepping in and making a scene when I’m just standing here?*

I looked at the Skeleton King suspiciously and cleared my throat.

By then, everyone who had been rushing around busily had frozen and was staring in our direction.

“Ahem. I’d like to say a few words in case anyone here doesn’t know who I am…”

“Jin Taekyung!”

“Lord Fuck!”

“Lord Sibu-leol!”

“…but I suppose that won’t be necessary.”

Well, as strange as it was to say it myself, by now, if there was a Hunter who didn’t recognize my face, I had to wonder whether they were actually a monster.

“Is, is that really Jin Taekyung?”

“I doubt there’s a fake Jin Taekyung.”

“Ah, that’s not what I meant…”

“It’s fine. That isn’t important right now, either.”

I turned toward the B-rank Hunter who had destroyed the car.

“From what I’ve seen, you appear to be the person in charge here. Is that right?”

“Y-Yes, that’s right. My name is Gwak Hangu, the Branch Leader of Ares Guild’s Yeokgok Branch.”

Not even the Bucheon Branch Leader, but one of the dozens of lower Branch Leaders beneath him was a B-rank Hunter.

It was a fresh reminder of Ares Guild’s talent pool and sheer size. Along with another fact I had briefly overlooked.

*Maybe because of their public image, but the atmosphere here is better than I expected.*

Ares Guild, I, and the Peace Guild were bound together by a terrible history.

But in the end, that battle had taken place beneath the surface. To people who knew nothing about it, the surface was peaceful and calm.

No. If anything, the eyes of the Ares Guild members here held expectation and even goodwill.

*Maybe we can build up our strength faster than Team Leader Choi expected.*

But something more important was waiting right now.

I pushed the thought that had suddenly crossed my mind aside and spoke to the Branch Leader.

“Let’s cut out all the side issues and get straight to the point.”

“Y-Yes?”

“Guild support is difficult right now, isn’t it? Ares Guild isn’t responsible for just one or two Gates, after all. You’re also sending personnel overseas.”

“Pardon?”

“Even if you send people now, they’ll arrive too late. That A-rank Hunter who’s on vacation has probably switched off his phone and pager and is having a good time. And if the people here rush in, there’s a high chance they’ll all die without even being able to perform a rescue. Am I right?”

“That, that’s not something we know…”

“Don’t give me that. What we don’t know is how long the people inside can hold out.”

The Branch Leader gasped.

“It’s been fifteen minutes since the mana levels first began rising. The team members inside might already be dying.”

“W-Wait a moment.”

The B-rank Hunter barely managed to stop me before continuing in a trembling voice.

“I know. I know that, too. But… outside intervention is a serious violation of Guild policy.”

“So?”

“Everyone here, including me, desperately wants to ask you for help. But we can’t. You already know that. You’ve heard about it.”

I did know.

Anyone who worked as a Hunter had to know how strict and difficult Ares Guild’s rules were.

Lee Jungryong had selected only the most capable Hunters from each rank and locked them inside a tall, enormous cage. The fact that no Guild would accept a Hunter expelled from Ares Guild wasn’t some vague urban legend.

“Ha…”

“Goddammit…”

Sighs and curses rose from various places. I stared at the Ares Guild members, then suddenly opened my mouth.

“One person? Or two?”

“Huh? What are you—”

“I have a feeling two people have died while you were hesitating.”

“Mr. Jin Taekyung!”

“Hey, you measuring over there. What are the mana levels now?”

Despite my arrival, one C-rank Hunter had been anxiously biting his nails in front of the measuring device. He now shouted as though screaming.

“Three times! It’s broken through three times the average mana level!”

“…!”

No one present failed to understand what that meant.

*Mutated Gate.*

The third Mutated Gate to erupt in the week since the new year began.

I clicked my tongue softly and looked straight at the Branch Leader.

“What are you waiting for? Open it.”

“…!”

“I wasn’t going to enter without the person in charge’s consent because it would be illegal. But people need to be saved, don’t they? So just say that I barged in while making a huge fucking scene and open it right now.”

His eyes squeezed shut. His tightly clenched fists trembled.

As I turned away from the silent Branch Leader, a trembling voice came from behind me.

“Let’s say… that I gave my consent.”

I thought he was a complete moron, but this put him at least in the category of a fool.

I let out a short laugh and left him with one final remark before striding toward the Gate.

“Call me if you get fired. The Peace Guild will take you in.”
```
