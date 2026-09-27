<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1182.txt",
      "sha256": "4e976edb51eeaa1c0492a4f3ee02b90bdebabb6cc6e186b51ae9f72eb898c2c0",
      "bytes": 12652
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5774977a50e9b32efcd98aa69e65a7227b2fcac539634f86079b646740dcb94d",
      "bytes": 2099
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2372eff4014bbbfe2875ceb74264c004f7f386d353a549f999d2b18a5d322a72",
      "bytes": 248683
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "e0eaa5b4bb4bc97005bacca5329452cbd413a7d0e11be374e57828acd640f2a9",
      "bytes": 951
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "7bd9bc0a6631b5dfbc64b158391fdc1df18c58f5e49e7921c245344b7b0681cc",
      "bytes": 688
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f66340d892ff45de57d0cbb577c72f78e861ddd786d6ef8b1165ae9d0351dd7d",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "75be68b72b39b5e6c6d782ce022a7bea8377ea56c3583b9e78d72e3a3d0c348a",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "a9aa270acab7971e3a24620d25b43941bc7765d1b2746bc6d96182c98777e3a4",
      "bytes": 700
    },
    {
      "path": "characters/Son of Heaven.md",
      "sha256": "39be589e0666614d52aedf47a5b1e16a22f55e8ef68768476d0e202c97f26ca8",
      "bytes": 684
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "603e3c49f5d38d12148c65f30dba06292ea6e50bd93d8155390005ac0494757a",
      "bytes": 295700
    }
  ],
  "estimated_tokens": 10469
}
-->

# Durable State Update — Chapter 1182

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
1 and safe_through 1182. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1182. Profile updates may replace only one
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
  "chapter": 1182,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1182,
    "continuity_sources": [1182],
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
    "The Murim allied forces split into three forces at the Qinghai-Xinjiang border, planning to rendezvous with the Imperial Army near Tianshan.",
    "A vast monster horde reached the allied vanguard near Tianshan, and battle began. Jin Wikyung leads the exhausted Jin Family of Taiyuan forces; Jin Mukyung, Mae Jonghak, four of the Ten Kings, and leaders of the Nine Sects and One Gang and the Five Great Families are present.",
    "Taekyung’s group crossed barren land in Xinjiang with no signs of life; the cause is unknown.",
    "Jeok Cheongang, Hyuk Mujin, Cheongpung, and Ju Hwaran know Taekyung is from another world. He has said he is human and around twenty-eight.",
    "Great Sir does not know Taekyung’s secret; Jeok leaves telling him to Taekyung.",
    "Bow Saint knows Taekyung’s secret and questions whether the Martial God’s letter is right.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete. The Grand Mage serves the Lord and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed. “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon. Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what it means remain unknown.",
    "Bow Saint grieves for someone she respected and admired, while denying that the person is Taekyung."
  ],
  "continuity_sources": [
    1181,
    1180
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "What caused the barren land around Taekyung’s group in Xinjiang?",
    "Who is the person Bow Saint misses?"
  ],
  "safe_through": 1181,
  "temporary_decisions": [
    "Render 대인 as Great Sir, following the established glossary."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 도사      | **Daoist**                                                      |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 시취 | **corpse stench** | The odor Taekyung recognizes from the covered body. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 황도십이궁 | **Twelve Palaces of the Zodiac** | Collective title for twelve Supreme Peak masters representing the imperial court. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 주체 | **Zhu Di** | The Emperor names himself as Zhu Di. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 팔황 | **Eight Directions** | Paired with the Nine Provinces as a broad geographic expression. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 1136
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a martial arts instructor to the Emperor, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, Baek Yeon prioritizes the Great Nation and its people over Murim’s interests, and is willing to dismantle Murim if it becomes a threat to them.
- **Voice:** Baek Yeon speaks with measured formality in public, but with the Emperor he shifts easily into familiar teasing and earnest, eloquent praise.
- **Relationships:** Baek Yeon is the Emperor’s trusted confidant and former martial arts instructor, and he is entrusted with protecting Zhu Bao; he commands the Embroidered Uniform Guard and treats Taekyung as a dangerous potential obstacle.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Deceased Thousand Captain of the Embroidered Uniform Guard, Jeong Hogun was a disciplined martial artist who led his guards in battle.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun served under Baek Yeon in the Embroidered Uniform Guard and is remembered by Jin Taekyung as a steadfast comrade who died protecting others.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1181
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1181
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1154
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Son of Heaven.md

# Son of Heaven (천자)

- **Safe through:** Chapter 1140
- **Aliases:** Emperor, Zhu Di
- **Role:** The Son of Heaven is the Emperor of Great Ming and Zhu Bao’s elder brother; he has ordered a personal expedition to Xinjiang and will not return to the palace until the traitors are rooted out.
- **Personality:** Coldly strategic and imperious, he is willing to break taboos to remain with his younger brother.
- **Voice:** Calm and commanding, with dry, understated humor.
- **Relationships:** Zhu Bao is his younger brother and heir; Jin Taekyung gave him the White Illusion Jiangshi Art; he killed Ma Sanbao.

## Korean source

```text
＃1182화



사방으로 퍼져 나가는 짙은 피 안개는 비단 사막 서쪽의 고원에서만 찾아볼 수 있는 것이 아니었다.

천리 밖 동쪽의 분지(盆地)에 펼쳐진 잔혹한 풍경 역시, 그곳과 다르지 않았으니까.

아니, 너무나도 닮아 있었으니까.

콰드드득!

전투는 격렬했다.

동시에 처절했다.

시야를 가릴 만큼 세찬 빗줄기 사이로 누구의 것인지 모를 핏물과 살덩어리가 비산하고, 낫처럼 길고 예리한 발톱과 잘 벼려진 창칼이 서로를 향해 날아들었다.

카아아앙!

불똥이 튀었다. 성인 장정의 두 배에 달하는 체구를 지닌 괴물들이 분노 섞인 포효와 함께 달려들었다.

- 그아아아!

통나무처럼 두꺼운 팔과 다리. 그리고 썩은 몸뚱어리에 매달린 서너 개의 머리까지.

원초적인 공포를 불러일으키는 그 괴이한 모습은 마주하는 것만으로도 등골을 서늘하게 만들었지만, 다음 순간 울려 퍼진 낮고 깊은 소리가 그들의 정신을 일깨웠다.

둥, 둥, 둥!

전고(戰鼓).

수십 명의 역사(力士)들이 온 힘을 다해 퍼트리는 그 거대한 울림이 광활한 분지를 뒤흔들었다.

얼어붙어 있던 손발을 녹이고, 서서히 꺼져 가던 용기에 숨을 불어넣었다.

“방(防)!”

힘찬 외침을 따라 펄럭이는 깃발.

그와 함께 수만의 군세가 일사불란하게 움직였다.

괴물들의 발톱은 인간의 살과 뼈 대신 철을 덧댄 방패를 갈랐고, 고슴도치처럼 빽빽한 방진을 구성하고 있던 창병들은 일장에 달하는 장창을 내질렀다.

콰득! 푸푸푸푹!

곳곳에서 솟구치는 피 분수.

그러나 그 핏물은 비단 적들만의 것이 아니었다. 

날카롭게 벼려진 창날로도 흠집 하나 나지 않은 상당수의 괴물들은, 앞을 가로막은 방패벽을 부수며 흐트러진 대열 사이로 뛰어들었으니까.

후우웅, 콰앙!

흙더미가 솟구쳤다.

불과 촌각 전까지만 하더라도 힘이 넘치던 육신은 한낱 살덩어리가 되어 튕겨 나가고, 그 비현실적인 광경을 눈앞에서 목격한 이들은 잠시 잊고 있던 공포를 떠올렸다.

그리고 바로 그 순간.

슈확!

허공으로부터 내리꽂힌 수십 줄기의 섬광이, 끝없이 돌격해나가던 괴물들의 앞을 가로막았다.

아니.

베었다.

서걱, 푸화아악!

가까스로 죽음을 면한 선두의 병사들은 부릅뜬 눈으로 안개처럼 번지는 녹색 핏물을 바라보았다.

정확히는, 조각난 괴물들의 시체 위로 떨어져 내린 그림자들을.

이질적으로 느껴질 만큼 환하게 빛나는 황금빛 갑옷과 그런 금의위(錦衣衛)들의 중심에 우뚝 서 있는 한 사내의 모습을.

“황제 폐하!”

그들은 숨길 수 없는 충정과 경외심을 담아 부르짖었다.

구주팔황과 사해오호를 아우르는 유일한 지배자이자, 하늘의 뜻을 받들어 천하 만민을 다스리는 어버이를 향해.

그리고 대명제국의 천자(天子), 주체는 그 부름에 답했다.

지금의 이 급박한 상황에서, 가장 효과적인 방식으로.

푸푹!

매의 그것임이 분명한 날개를 한껏 접은 채, 마치 벼락처럼 허공에서 내리꽂히던 괴물의 몸뚱어리가 부르르 떨렸다.

“감히 누구에게 달려드는 것이냐.”

천자는 놀라우리만치 담담한 음성과 함께, 괴물의 미간 깊숙이 박아넣은 검을 비틀었다.

“허나 너 역시 한때는 짐의 백성이었을 터.”

콰득.

“이만 편히 쉬거라.”

마지막을 알리는 한 줄기 파육음과 함께 괴물의 움직임이 완전히 멎자, 이 광경을 지켜보던 수만의 금위군(禁衛軍)은 불현듯 뱃속 깊은 곳에서 치밀어오르는 뜨거운 무언가를 느꼈다.

천자가 누구인가.

그들의 주군이며 대륙의 주인이다.

한데 감히 올려다볼 수도 없던 지고지순한 존재가 자신들과 함께 싸우고 있다.

어깨를 나란히 한 채, 적의 핏물을 뒤집어쓰며.

또 다른 누군가는 고작 그것이 전부냐며 코웃음 칠 수도 있겠으나, 그들에게는 그것만이 전부였다.

목숨을 기꺼이 내던질 수 있는 이유로는.

“황제 폐하 만세!”

“대명제국 만세!”

수백에서 수천. 수천에서 수만, 그리하여 마침내 하나가 된 함성과 함께 황군(皇軍)은 돌격했다.

그리고 그런 그들의 뒷모습을 천자는 말없이 지켜보았다.

그를 가까이에서 호위하던 한 젊은 장수가 입을 열기 전까지.

“청컨대, 소장이 감히 한 말씀 올려도 되겠나이까.”

천자가 고개를 저었다.

“불허한다.”

한 치의 망설임도 없는 대답.

그러나 젊은 장수는 굴하지 않았다.

“이만 돌아가시지요. 이곳은 위험합니다.”

“짐이 한 말을 듣지 못하였느냐?”

“분명히 들었사옵니다.”

“그럼 이 죄를 어찌 치르려 하느냐?”

“무슨 벌이든 달게 받겠습니다. 다만, 폐하의 옥체를 보존하신 후에 형을 집행해주시길 간청드리는 바입니다.”

정중하면서도 당당한 그 태도에, 천자는 그만 실소했다.

“금의위 천호(千戶) 따위가 감히 짐의 말을 거스르려 하다니, 황실의 법도가 단단히 흐트러졌군. 그렇지 않나?”

그때, 어디선가 홀연히 나타난 중년인이 불쑥 입을 열었다.

“황실 그 자체가 무너지는 것보다, 황실의 법도가 흐트러지는 것이 백번 낫지 않겠습니까.”

당장 대역죄인으로 몰려도 할 말이 없는 불경스러운 대답이었지만, 천자는 눈썹 하나 까딱하지 않았다.

은빛 언월도를 든 저 중년인이야말로, 천하의 그 누구보다 황실의 수호를 위해 힘써왔던 충신이었으므로.

“왔는가, 백연.”

간단하게 군례를 올린 금의위 지휘사, 백연이 앞서 흘러나온 천자의 말을 정정했다.

“올 수밖에 없었지요.”

“희한하군. 짐을 포함한 그 누구도 그대를 부르지 않았거늘.”

“하면 안전한 후방에 계셔야 할 폐하께서는 왜 이곳에 계십니까?”

“그대가 누구의 부름 없이도 스스로 이곳에 온 것과 같은 이유다.”

순간 멈칫한 백연이 헛웃음을 흘렸다.

“우문(愚問)을 현답(賢答)으로 돌려주시니, 소신으로서는 더는 드릴 말씀이 없나이다.”

그래, 정말이지 어리석은 질문이었다.

금의위 지휘사인 그가 천자를 보호하기 위해 이곳으로 왔듯이, 천자는 자신을 따르는 백성을 지키고자 움직였다.

대의(大義)가 아닌, 인의(人義)를 위해서.

‘인의, 인의라.’

오랫동안 잊고 있던 단어다.

들끓는 혈기와 타고난 군재(軍才)를 바탕으로 전장을 질주했던 제국의 사황자는 암천의 짙은 그림자가 황실에 드리워진 이후 사라졌으니까.

천자는 냉정해야 했고, 무정해야 했다. 그것이 옳은 방향이라 여겼다. 모든 문제를 해결할 수 있는 유일한 열쇠라고 생각했다.

적어도 몇 달 전, 한 사람을 알게 되기 전까지는.

‘진태경.’

그는 실로 자유분방했다.

무엇이 앞을 가로막아도 그저 온 힘을 다해 나아갔다.

단순히 용맹해서?

틀렸다.

그가 남들과 같은, 아니 그보다 더욱 큰 두려움과 고통을 느끼고 있음에도 그것이 인의라 믿기 때문이었다.

진태경이 나아가는 길은 좁았으나, 올곧았다.

그리하여 마침내 모두에게 닿았다. 수많은 발걸음을 이곳까지 이끌었다.

“짐보다 낫군. 천자인 것이 부끄러워질 만큼.”

문무백관이 들었다면 조야가 발칵 뒤집혔을 뇌까림과 함께, 천자는 늘어트렸던 검을 다시금 곧추세웠다.

그리고 문득, 앞서 자신을 만류했던 금의위의 젊은 장수를 향해 물었다.

“그대의 뜻은 아직도 변함없는가?”

장수가 흔들림 없는 목소리로 입을 열었다.

“송구하옵게도, 그러합니다.”

“그렇다면 좋다. 지금 즉시 그 뜻에 따라 물러날 터이니, 그대는 짐의 곁에서 단 한 시도 떨어지지 말라.”

생각지도 못한 말에 장수가 멈칫한 그때, 천자가 힘 있는 목소리로 덧붙였다.

“허나, 우리가 물러나는 방향은 뒤가 아닌 앞이 될 것이다.”

“폐하.”

“짐은 천자다. 만백성의 어버이이며, 어버이는 결코 피 흘리는 자식을 외면하지 않는다. 그것이 바로 하늘의 뜻이다.”

“……!”

“다시 묻겠다, 그대의 뜻은 아직도 변함이 없는가?”

찰나의 침묵이 흐른 뒤, 젊은 장수가 무릎을 꿇었다.

“신, 금의위 천호 정호군. 지엄하신 황제 폐하의 명을 받드나이다.”

“짐의 뒤를 따르라. 길을 연다.”

“존명(尊命)-!”

정호군 혼자만의 대답이 아니었다.

어느덧 천자의 주위를 빈틈없이 에워싼 일천의 금의위가 일거에 내지른 함성은 일순간 전장을 떨어 울렸다.

중과부적(衆寡不敵)의 형세에 몰려 빠르게 허물어지고 있는 금위군들의 머리 위를 스치듯 지나쳐, 그 너머에 도사린 진정한 적들에게까지 닿을 만큼.

쿵. 쿵.

그 어떤 빛도 반사되지 않는 칠흑빛 갑주가 움직일 때마다 울려 퍼지는 둔탁한 소음.

깊게 눌러쓴 투구 사이로 붉게 물든 눈이, 그 아래로 드러난 입에서는 죽은 자의 시취(屍臭)가 흘러나오고 있었다.

“흑귀(黑鬼)……!”

한 기, 한 기가 초절정 고수나 다름없다는 진정한 괴물.

그 숫자가 무려 스물에 달한다는 사실을 확인한 수많은 눈동자들이 잘게 떨려 오던 그때, 천자의 입술 사이로 벼락 같은 외침이 터져나왔다.

“십이궁(十二宮)에게 명하노라!”

바로 그 순간.

콰드드득!

전장 곳곳에서 십여 줄기의 섬광이 솟구쳤다.

그리고 앞을 막아서는 괴물들을 단숨에 짓뭉개며 천자의 앞까지 도달한 열두 명의 남녀가 깊게 고개를 숙였다.

황실을 지탱하고 밝히는 기둥이자 별, 황도십이궁(黃道十二宮). 

황궁에서의 혈사 이후, 천자의 지휘 아래 새롭게 정립된 황실 직속의 초절정 고수들은 형형하게 빛나는 눈빛으로 자신들의 주군을 바라보았다.

“하명하소서.”

천자는 크게 심호흡했다.

이 전투가 끝났을 때, 과연 이들 중 몇이나 살아남을 수 있을까.

아니, 저 끔찍하리만치 강대한 적들을 상대로 감히 승리를 점칠 수나 있을까.

‘예전의 짐이었다면, 과연 어찌했을 것인가.’

천자는 불현 듯 떠오른 이 의문에 대한 답을 이미 알고 있었다.

그는 망설임 없이 퇴각했을 것이다. 

수만의 금위군을 사지로 밀어 넣는 한이 있더라도.

하지만 한 사람의 행동으로 인해 뒤바뀐 것은 이 세상만이 아니었다.

천자 역시 새롭게 태어났다. 

비록 모산파의 무학을 받아들임으로써 육신은 죽은 것과 진배 없게 되었으나, 그의 심장과 피는 그 어느 때보다 뜨겁게 끓어오르고 있었다.

이 자리의 모든 이들처럼.

그를 다시 일깨워 준 그, 진태경처럼.

그리고 만약 그가 이 자리에 있었다면, 분명 이렇게 말했을 것이다.

“모조리 쓸어 버려라.”

예법 따위는 조금도 찾아볼 수 없는, 그래서 더욱 선명한 자유를 느끼며 천자는 피로 물든 대지를 질주했다.

쐐애애애액!

번뜩이는 황금빛 물결이, 유성의 꼬리처럼 길게 늘어졌다.



* * *



진태경은 불현듯 고개를 들었다.

어느샌가 검게 물든 하늘 위로 두 줄기의 빛줄기가 스쳐지나가고 있었다.

‘유성?’

그리 흔한 일도, 그렇다고 매우 드문 일도 아니다.

하지만 어째서일까.

진태경은 욱신거리는 가슴을 짓눌렀다.

그리고 오랫동안 제대로 된 잠을 청하지 못했다.

밤이 물러가고 서광이 찾아온 뒤에도, 일행과 함께 그 지긋지긋한 사막을 벗어난 후에도.

만년설이 쌓인 산과 들을 지나, 모든 연합군이 합류하기로 했던 장소에 도착한 뒤에도.

찾아오는 이들은 없었다.

하루, 또 하루가 지나도.
```

## Final English reading copy

```markdown
# Chapter 1182

The thick mist of blood spreading in every direction wasn’t found only on the plateau west of the desert.

The brutal scene unfolding in a basin a thousand li to the east was no different.

No—it was all too similar.

*Crack!*

The battle was fierce.

And desperate.

Through the torrential rain, heavy enough to obscure the field, blood and chunks of flesh flew—no one could tell whose. Long, razor-sharp claws like scythes and finely honed spears and blades rushed at one another.

*Clang!*

Sparks flew. Monsters twice the size of grown men charged with furious roars.

*Graaah!*

Arms and legs thick as logs. Three or four heads hanging from rotting bodies.

Their grotesque appearance inspired a primal fear, chilling the spine at a glance. But the low, deep sound that rang out the next moment snapped them back to their senses.

*Boom. Boom. Boom.*

A war drum.

Dozens of strongmen poured all their strength into its thunderous beat, shaking the vast basin.

It thawed frozen hands and feet and breathed life into courage that had begun to fade.

“Defend!”

At the forceful shout, a flag flapped in the rain.

The tens of thousands of troops moved as one.

The monsters’ claws tore into iron-plated shields instead of human flesh and bone. Spearmen arranged in a bristling formation thrust their long spears, each a zhang from end to end.

*Crack! Splurt!*

Fountains of blood erupted here and there.

But it wasn’t only the enemy’s blood.

Many monsters remained unmarked even by the sharpened spearheads. They smashed through the shield wall in their path and leaped into the gaps in the broken ranks.

*Whoosh! Boom!*

Clods of earth burst into the air.

Bodies that had been full of strength a moment ago were flung away as mere chunks of flesh. Those who witnessed the unreal sight remembered the fear they’d briefly forgotten.

And right then—

*Shing!*

Dozens of streaks of light plunged down from the sky, blocking the monsters’ endless charge.

No.

They cut them down.

*Slice! Splatter!*

The soldiers at the front, who’d only just escaped death, stared wide-eyed at the green blood spreading like mist.

More precisely, at the shadows descending over the monsters’ mangled corpses.

At the golden armor shining almost unnaturally bright—and at the man standing tall in the midst of those Embroidered Uniform Guards.

“Your Majesty!”

They cried out, unable to hide their loyalty and reverence.

They called to the sole ruler of the Nine Provinces and Eight Wastes, the Four Seas and Five Lakes, the father who governed all under heaven in accordance with the will of Heaven.

And the Son of Heaven of the Great Ming Empire, Zhu Di, answered their call.

In the most effective way possible for this urgent moment.

*Thud!*

The monster’s body shuddered. Its wings, unmistakably those of a hawk, were folded tight as it plunged from the sky like a bolt of lightning.

“How dare you charge at me?”

The Son of Heaven spoke with astonishing calm as he twisted the sword buried deep between the monster’s brows.

“But you, too, were once one of my people.”

*Crack.*

“Rest in peace.”

With one final, wet crunch, the monster stopped moving. The tens of thousands of Imperial Guards watching felt something hot rise from deep in their bellies.

Who was the Son of Heaven?

Their lord. The master of the continent.

And yet this supreme being, someone they scarcely dared look up to, was fighting alongside them.

Shoulder to shoulder, drenched in the enemy’s blood.

Someone else might scoff and ask if that was all it took. But to them, it was everything.

Everything they needed to be willing to give their lives.

“Long live Your Majesty!”

“Long live the Great Ming Empire!”

Hundreds became thousands, then thousands became tens of thousands. At last, one unified roar rose up as the Imperial Army charged.

The Son of Heaven watched them go in silence.

Until a young officer guarding him nearby spoke.

“Your Majesty, may this humble officer dare to say something?”

The Son of Heaven shook his head.

“Denied.”

The answer came without a moment’s hesitation.

But the young officer didn’t back down.

“Please return. It’s dangerous here.”

“Did you not hear what I said?”

“I heard you clearly.”

“Then how do you intend to answer for this crime?”

“I will accept any punishment. But I beg Your Majesty to preserve your sacred person first, and carry out the sentence afterward.”

The young officer’s manner was respectful yet unflinching. The Son of Heaven let out a quiet laugh.

“A mere Thousand Captain of the Embroidered Uniform Guard dares to defy my word. The laws of the imperial house must have fallen into disarray. Wouldn’t you agree?”

A middle-aged man who had appeared out of nowhere spoke up.

“Wouldn’t it be a hundred times better for the laws of the imperial house to fall into disarray than for the imperial house itself to fall?”

It was a disrespectful answer that could have seen him branded a traitor on the spot. Yet the Son of Heaven didn’t so much as raise an eyebrow.

The middle-aged man holding a silver crescent-bladed halberd was the most loyal subject in the world when it came to protecting the imperial house.

“You came, Baek Yeon.”

Baek Yeon, Commander of the Embroidered Uniform Guard, gave a simple military salute and corrected the Son of Heaven’s earlier words.

“I had no choice.”

“How strange. No one called for you—not even me.”

“Then why is Your Majesty, who ought to be in the safe rear, here?”

“For the same reason you came here of your own accord.”

Baek Yeon paused, then gave a dry laugh.

“You’ve turned a foolish question into a wise answer. I have nothing more to say.”

Yes. It had been a foolish question.

Just as Baek Yeon had come here to protect the Son of Heaven, the Son of Heaven had moved to protect the people who followed him.

Not for some grand cause, but out of compassion for his people.

*Compassion. Compassion…*

It was a word he hadn’t thought of in a long time.

The Empire’s fourth prince, who’d once raced across battlefields on the strength of his burning blood and innate military talent, had disappeared after the dark shadow of Dark Heaven fell over the imperial house.

The Son of Heaven had to be cold. He had to be heartless. He’d believed that was the right course—the only key that could solve every problem.

At least, until a few months ago, when he met one man.

*Jin Taekyung.*

He was utterly free-spirited.

No matter what stood in his way, he simply pushed forward with all his strength.

Was it because he was brave?

Wrong.

He felt fear and pain just like everyone else—perhaps even more than they did. But he pressed on because he believed it was the compassionate thing to do.

The path Jin Taekyung walked was narrow, but straight.

And in the end, it had reached everyone. It had led countless people all the way here.

“He’s better than I am. Enough to make me ashamed to be the Son of Heaven.”

With that mutter—one that would have sent the court into an uproar had the civil and military officials heard it—the Son of Heaven raised the sword he’d let hang at his side.

Then he turned to the young Embroidered Uniform Guard officer who’d tried to stop him.

“Has your resolve still not changed?”

The officer replied in a steady voice.

“With all due respect, no.”

“Very well. I will withdraw in accordance with your wishes, at once. In return, you are not to leave my side for even a moment.”

The officer faltered at the unexpected words. The Son of Heaven added, his voice strong,

“But the direction we withdraw will be forward—not back.”

“Your Majesty.”

“I am the Son of Heaven. The father of all the people. A father never turns away from his children when they’re bleeding. That is the will of Heaven.”

“……”

“I ask you again. Has your resolve still not changed?”

After a moment’s silence, the young officer went down on one knee.

“I, Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, receive the command of Your Majesty, the august Emperor.”

“Follow me. We’ll open a path.”

“As you command!”

Jeong Hogun wasn’t the only one to answer.

The thousand Embroidered Uniform Guards who had now closed ranks around the Son of Heaven let out one mighty roar, and the battlefield shook.

Their cry swept over the heads of the Imperial Guards, whose lines were rapidly collapsing under the overwhelming odds, and reached even the true enemy lying in wait beyond them.

A dull thud rang out with each movement of the pitch-black armor that reflected no light.

Red eyes glowed beneath deeply lowered helmets. From the mouths visible below them came the stench of the dead.

“Black Ghosts…!”

Each one of them was a true monster, no different from a Supreme Peak master.

When countless eyes began to tremble at the sight of no fewer than twenty of them, a thunderous cry burst from the Son of Heaven’s lips.

“I command the Twelve Palaces!”

At that very moment—

*Crack!*

More than ten streaks of light shot up from across the battlefield.

Twelve men and women reached the Son of Heaven in an instant, crushing the monsters that stood in their way. They bowed deeply before him.

The pillars and stars that upheld and illuminated the imperial house: the Twelve Palaces of the Zodiac.

After the bloodshed in the imperial palace, these Supreme Peak masters had been newly organized under the Son of Heaven’s command as a force directly under the imperial house. Their eyes shone brightly as they looked to their lord.

“Give your command.”

The Son of Heaven took a deep breath.

When this battle was over, how many of them would still be alive?

No—could anyone even dare to predict victory against enemies so terrifyingly powerful?

*What would the old me have done?*

The Son of Heaven already knew the answer to the question that had suddenly come to mind.

He would have retreated without hesitation.

Even if that meant sending tens of thousands of Imperial Guards to their deaths.

But the actions of one man had changed more than just this world.

The Son of Heaven had been reborn, too.

Though he’d taken up the Maoshan Sect’s martial arts and his body was now no different from a dead man’s, his heart and blood burned hotter than ever.

Just like everyone gathered here.

Just like the man who’d awakened him once again: Jin Taekyung.

And if that man were here, he would surely say this:

“Wipe them all out.”

Feeling a freedom all the clearer for its utter lack of decorum, the Son of Heaven raced across the blood-soaked earth.

*Whoooosh!*

A brilliant golden wave stretched long behind him, like the tail of a meteor.

* * *

Jin Taekyung suddenly raised his head.

Two streaks of light had just passed across the sky, now black with night.

*A meteor?*

It wasn’t exactly common, but it wasn’t all that rare, either.

And yet, why?

Jin Taekyung pressed down on his throbbing chest.

For a long time, he couldn’t manage a proper night’s sleep.

Not after night gave way to dawn and the first light appeared. Not after he and his companions finally left that damned desert behind.

Not even after they passed through mountains and fields blanketed in perennial snow, and reached the place where all the allied forces were supposed to rendezvous.

No one came.

A day passed, then another.
```
