<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0850.txt",
      "sha256": "ab9dc7fb4a96bb62a41faef6565fc49c45fb3ff2a6e3dd3662bbf29bc725268f",
      "bytes": 14249
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "69b91997cc468259bf73314ddb5e0d7c98a7361ba6be311d99ab8cb75ab3473d",
      "bytes": 782
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6b3a5cc8f26f77fb300434ce4eb95cd4b17da81997c54bf458d11750dd5e8a9d",
      "bytes": 227660
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "97a9e934d335cfe961a3eebe4b35d82a433a6c41fb7d4ef3debd4d27cf5bd6d8",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "1573261d334a54b506a8f7d5ba3e58b0dd50a787b1041a46d2449307a6b4d6e3",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c7560e60e762f1bfeb4b91c2f44e97e095847f916db7f27828a401debb620095",
      "bytes": 1573
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "9c3dab58222ed8b2603aca3888fdba0e00aaa07390092f2f2bc5a3457d0387ee",
      "bytes": 801
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "d747c3dc7bc73d48eb5a85e4047462327e1d9e14ba3a1e154ff2115ebab0a826",
      "bytes": 752
    },
    {
      "path": "characters/Namho.md",
      "sha256": "123661aa1bea471cdb19d86ee0877942b6a68cb56c75011fbed273acc7e1c648",
      "bytes": 936
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "ed2dee82db4b9f37d93a1d9461dba762cd51e06cc268c10ab0d276cb1000f578",
      "bytes": 914
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "2bd31f98c72877821bd75841761672402aaecd5dc5b586d0fcb83bb6655ca915",
      "bytes": 715
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e355e81484ae949dc8e78222090e84cb4d51822836709e9b1a9310bffea46b83",
      "bytes": 252668
    }
  ],
  "estimated_tokens": 11491
}
-->

# Durable State Update — Chapter 850

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
1 and safe_through 850. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 850. Profile updates may replace only one
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
  "chapter": 850,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 850,
    "continuity_sources": [850],
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
    "Jin Taekyung remains incompletely recovered; Jeok Cheongang’s treatment improved his condition, but pain persists in his lower dantian.",
    "The Divine Physician secretly found Blood Soul Gu, a rare gu poison from deep in Nanman, in the dead City Lord Won Gyun’s body; the public diagnosis remains sudden natural death."
  ],
  "continuity_sources": [
    848,
    849
  ],
  "open_questions": [
    "Who placed Blood Soul Gu in Won Gyun’s body, and how did it contribute to his death?",
    "Will Jin’s lower-dantian injury improve further, or remain beyond full recovery?"
  ],
  "safe_through": 849,
  "temporary_decisions": [
    "Render 고독 as “gu poison.”",
    "Render 혈혼고 as “Blood Soul Gu.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 무신     | **Martial God**               | —              |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 선배     | **Senior**                                   |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 평화 | **Peace Guild** | Guild name. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 야명주 | **night-shining pearls** | Pearls embedded in the cavern ceiling that provide light. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 849
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 840
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 849
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 849
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and distant imperial relative who, while still under punishment, has been temporarily appointed acting City Lord of Sichuan Province by imperial order.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor, and Jin Taekyung is the benefactor who saved his life and can leverage Wongong’s temporary office.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 843
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 849
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 849
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 844
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

## Korean source

```text
＃850화



혈혼고(血魂蠱).

남호를 통해 알게 된 고독의 정체는 그 이름부터가 불길하기 짝이 없었다.

‘애초에 고독을 직접 보는 것도 처음이지만.’

내심 중얼거린 나는 신의의 손바닥 위에서 꿈틀대는 작은 생물체를 유심히 살폈다.

좁쌀보다도 훨씬 작은 크기에 실처럼 가느다란 몸통은 온통 핏빛이다.

척 보기에도 평범한 사람의 육안(肉眼)으로는 판별할 수 없을 것 같은 그것은, 계속해서 신의의 살갗을 파고들기 위해 몸부림쳤다.

마치 그것만이 유일한 존재 이유이자 목적인 것처럼.

“처음부터 주의하지 않았더라면 꼼짝없이 당할 뻔했습니다. 작은 몸체에 비해 힘이 엄청나더군요.”

스슥, 스스슥!

마치 그 말을 알아듣기라도 한 것일까.

더욱 강해진 몸부림과 함께 도망치려는 혈혼고를 조심스럽게 감싼 신의는, 자그마한 호리병을 꺼내 집어넣고 단단히 마개를 봉했다.

그리고 몇 번이나 혹시 모를 틈새를 확인한 후에야 손에 끼고 있던 두터운 가죽 장갑을 벗었다.

“혈혼고라. 지난 세월 동안 스승님께 수많은 가르침을 받았지만…… 솔직히 이런 종류의 고독은 저도 처음입니다.”

신의의 뇌까림에 남호가 고개를 끄덕였다.

“그럴 수밖에 없을 거요. 혈혼고는 남만에서도 알려진 바가 극히 드문 독물(毒物)이니까. 아니, 정확히는 그 이름을 기억하는 이들이 이제 얼마 남지 않았다고 해야 옳겠구려.”

“그 말씀은…….”

“아주 오래전의 일이오. 당시의 남만은 세 발 달린 솥과 같은 형국으로 갈라져 끔찍한 전쟁을 벌이고 있었고, 그 과정에서 혈혼고의 존재가 처음으로 알려졌지.”

나로서는 모를 수가 없는 이야기였다.

남만에 머무르며 이미 몇 번이나 들었고, 과거로 거슬러 올라가면 내 사문인 열화문과도 맞닿아 있는 사건이었으니까.

입에서 입으로, 얼마 남지 않은 기록으로 전설처럼 전해져 내려오는 과거의 이야기.

그리고 그 중심에는 늘 빠지지 않고 등장하는 한 문파가 있었다.

“……오독문(五毒門).”

신음하듯 중얼거린 나는 남호를 바라보며 말을 이었다.

“혈혼고의 시작이, 오독문이라는 뜻입니까?”

“까마득한 과거의 일이니 섣불리 확신할 수는 없네. 그러나 내가 남만에 머무르며 보고 들은 것들이 모두 사실이라면, 오독문이 숱한 시도 끝에 만들어 낸 독물 중 하나가 바로 혈혼고지.”

“하지만 독혈지(毒血地)에서도 저런 건 본 적이 없었는데요.”

“고독이란 생물은 본래 깊고 은밀한 곳을 좋아하는 법. 제아무리 벌집 쑤시듯 독혈지를 누볐다 해도 쉽게 눈에 띄었겠나.”

맞는 말이었다.

천년지주(天年蜘蛛)를 포함한 온갖 기이한 괴물들이 득실거리던 독혈지다.

그 혼란스러운 상황 속에서, 그것도 혈혼고처럼 육안으로 식별하기 힘든 생물체까지 일일이 파악하는 것은 무리였다.

“오독문이라면 노부도 들어본 적이 있네. 본문의 사조(四祖) 중 한 분께서 남만에 관한 짤막한 기록을 남겨 놓으셨지.”

불쑥 입을 연 적천강이 깊게 가라앉은 눈빛으로 혈혼고를 가둔 호리병을 응시했다.

“한데 저건 평범한 고독과는 너무 거리가 멀어. 대침에 몸통이 관통당해도 살아남을 정도로 생명력이 끈질기고, 그렇다고 숙주를 절명시킬 만큼의 절독을 품은 것도 아니라더군.”

“그렇다면 더더욱 혈혼고가 맞습니다. 적 선배께서 생각하시는 고독이란 일정 주기로 해약(解藥)을 복용한다면 아무런 문제도 없지요.”

“그것이 모두가 알고 있는 사실이지.”

“하지만 혈혼고는 다릅니다. 일반적인 고독이 숙주를 협박과 조종하기 위한 목적으로만 쓰인다면, 오독문이 저 끔찍한 독물을 만들어 낸 이유는 단 하나뿐입니다.”

모두의 시선 속에서, 남호가 참았던 숨과 함께 뒷말을 토해 냈다.

“숙주의 죽음. 어떤 의미로는 완벽에 가까운 암살.”

“……!”

“오랜 세월 동안 남만에 머무르며 수많은 정보를 수집했습니다. 얼마 남지 않은 기록을 샅샅이 뒤지고, 각 부족에서 가장 늙고 지혜로운 이들을 찾아갔지요. 그들이 들려주는 이야기 속에서 진실을 더듬고, 그 진실 속에서 혹시 모를 허구를 걸러냈어야 했습니다.”

정마대전이라 명명된 거대한 전란이 종결된 어느 날, 무신(武神)이 홀연히 사라졌다.

수많은 이해타산과 감정으로 얽힌 수백, 수천 개의 문파가 구심점을 잃자 허물어지는 것은 당연한 수순이었을지도 모른다.

무림맹의 해산.

하지만 은영각의 뿌리는 천하 곳곳에 남아 있었다. 조금씩 허물어지는 어느 낡은 객잔에도. 사람으로 붐비는 대로변에도.

그리고 독와 맹수들이 들끓는 남만(南蠻)의 오지에도.

남호는 그중 가장 깊고, 오래된 뿌리 중 하나였다.

“오독문과 남만야수궁 간의 전쟁은 실로 치열했습니다. 백중세(伯仲勢)를 이룰 때도 있었고, 어느 한쪽이 우세할 때도 있었지요.”

백 년간 이어진 전란이었다고 했다. 우물과 강에는 독이 풀렸고, 남만야수궁의 전사와 맹수들은 오독문의 독인(毒人)을 베고 물어뜯었다.

“남만 전체가 독과 불길에 휩싸였습니다. 이대로 간다면 승자와 패자가 아닌, 공멸(共滅)만이 기다리고 있었겠지요.”

남호가 적천강과 나를 번갈아 바라보며 덧붙였다.

“어느 날, 한 이방인이 나타나기 전까지는.”

천하를 주유하던 당대의 열화문주는 남만에 닿자마자 성대한 환대를 받았다.

오독문의 전사 일백은 독과 암기를 이용해서 감히 자신들의 영역에 찾아온 이 낯선 이방인을 환영해 주었고, 그 이방인은 화끈하게 모든 것을 불태워 버린 뒤 남만야수궁에 합류했다.

“열화문주의 합류로 전세가 급격하게 기울자, 오독문은 더 이상 물러설 곳이 없다는 것을 깨달았을 겁니다. 시간이 흐를수록 더욱 끔찍하고 악독한 것들을 풀어놓기 시작했으니.”

잃어버릴 것조차 사라져 가는 이들에게 남은 것은 독기뿐이다.

오독문은 애뇌산 깊숙한 곳에 가장 은밀하고 위험한 장소, 독혈지에서 마지막 반격을 준비했다.

“전쟁이 막바지에 달할 무렵, 남만야수궁에서 가장 뛰어난 전사들이 하나둘씩 죽어 갔습니다. 독과 약에 통달한 의원도, 영험한 제사장도 그 이유를 몰랐다고 하더군요.”

남호의 말을 묵묵히 듣고 있던 신의가 어두운 얼굴로 입을 열었다.

“그랬을 겁니다. 별다른 부상조차 보이지 않았을 테니까.”

“맞소. 그건 중독도 역병도 아니었소. 남만야수궁이 그 원인을 깨달은 것은, 그렇게 죽은 전사들의 숫자가 일백을 넘어섰을 때였지.”

“제아무리 혈혼고의 움직임이 은밀하고 크기가 작아 발견하기 어렵다 한들, 그 정도의 사람들이 희생되었다면 더 빨리 발견할 수 있었을 텐데요.”

“나도 그렇게 생각했소. 하지만 그럴 만한 이유가 있었더군.”

작게 고개를 내저은 남호가 말을 이었다.

“자그마치 백 년간 이어진 전란에 모두가 지쳐 있었소. 평화라는 단어는 빛이 바래진 지 오래였고, 죽음이 곧 안식으로 여겨지던 시대. 그런 상황에서 일부 전사가 광증(狂症)을 앓는 것은 어찌 보면 당연한 일이었겠지.”

“광증…… 말입니까?”

“맞소. 그들 중 대부분이 어느 날은 마치 실성한 사람처럼 굴다가, 어느 날은 누구보다 용맹하게 싸웠다고 했소.”

신의가 탄식하듯 뇌까렸다.

“성주. 성주의 증상이 바로 그러했습니다. 처음 들었을 때는 그저 애첩을 잃은 탓에 생긴 마음의 병인 줄만 알았지요.”

“혈혼고는 심력(心力)이 약해진 숙주 안에서 더욱 강해지니, 어느 정도 연관은 있을 거요.”

“하면 남만야수궁에서는 그 사실을 어찌 알게 된 겁니까?”

“오독문의 장로를 생포하여 심문하는 과정에서 그에 관한 정보가 나왔다고 했소. 처음에는 십이지장과 혈도를 누비며 미약한 독으로 환청과 환각을 불러일으키다가, 끝내는 뇌수를 조금씩 파먹으며 숙주를 죽음으로 몰아간다더군.”

“……!”

“전사마다 죽음을 맞이하는 시기도 제각각이었소. 짧게는 반년, 길게는 수년간 버티는 이들도 있었다지.”

“숙주의 심신(心身)이 허약해질 때에야 비로소 행동을 개시하는 것들이군요.”

“맞소. 다만 그 살상력과 소요시간이 오독문이 처음 원했던 수준에는 턱없이 못 미쳤고, 그래서인지 오독문이 멸문(滅門)을 맞이하기 전까지 개량해 낸 개체 수가 그리 많지 않았다더군. 내가 알아낸 정보는 이게 전부요.”

남호의 마지막 말을 끝으로 무거운 침묵이 내려앉았다.

누구도 입을 열지 않았으나, 다른 이들의 생각을 읽는 것쯤은 그리 어렵지 않았다.

자그마치 백여 년간 남만을 피로 물들였던 과거의 대전쟁.

그리고 오랜 시간을 거슬러, 무림인도 아닌 대국의 관리에게서 다시 한번 모습을 드러낸 혈혼고.

나는 지그시 눈을 감으며 마음속으로 뇌까렸다.

아니, 혈혼고가 남만에서 비롯되었음을 알게 된 그 순간부터 줄곧 머릿속에 맴돌던 그 두 글자를 소리 내어 내뱉었다.

“암천.”

어두웠던 눈앞이 밝게 갠다. 눈을 뜨자 은은한 야명주의 불빛 아래에서 나를 바라보는 세 사람의 얼굴이 보인다.

“이미 남만에서 거의 잊힌 혈혼고가 중원까지 흘러들어올 가능성은 그것뿐입니다. 틀림없이 놈들 짓이에요.”

적천강이 가라앉은 목소리로 입을 열었다.

“남천마후.”

“무려 수십 년입니다. 암천이 남만에 발을 디디고, 독혈지에서 때를 기다리고 있던 것이. 혈혼고를 찾아낼 시간은 충분해요.”

“충분하지. 아니, 차고 넘치지.”

작게 고개를 끄덕인 적천강이 물었다.

“하지만 놈들이 무엇을 위해서 이 자를 해한단 말이냐?”

“그건…….”

나는 말꼬리를 흐리며 사천성주의 시신을 내려다보았다.

싸늘하게 식어 있는 팔과 다리. 백지처럼 새하얗게 물든 얼굴에는 그 어떤 고통의 흔적도 없었다.

그래, 적천강의 질문이 핵심이다.

놈들은 무슨 이유로 이 자를 죽인 것일까. 그것도 이토록 은밀한 방법을 써 가면서까지.

비록 성주라는 높은 관직에 있었으나 단지 그뿐이다.

여느 곳에서나 볼 수 있는, 적당히 탐욕스럽고 부패한 관리.

암천이 마음만 먹는다면 주머니 속의 동전처럼 빼낼 수 있는 목숨이었다.

‘그런데 이렇게까지 해야만 했던 이유는 무엇이었을까.’

성주가 사천혈사 당시 관병들을 움직여 우리를 도와서?

문득 그런 추측이 뇌리를 스쳤지만, 이내 고개를 저었다.

아니다. 그에 대한 보복이었다면 오히려 더 참혹한 죽음을 내리는 것이 백배 나았을 것이다.

성주씩이나 되는 고위 관료라 해도, 두 번 다시 암천에 대적하지 못하도록 온 천하에 각인시킬 수 있을 테니까.

스스로 무림과는 동떨어졌다 생각하는 그들마저 공포를 느낄 수 밖에 없을 테니까.

‘하지만 굳이 이런 방식을 택했다는 건…….’

다른 뭔가가 있다. 아직 알려지지 않은, 암천이 원하는 진정한 목표가.

그리고 꼬리에 꼬리를 물고 이어진 생각이 거기까지 다다른 그 순간.

저벅.

어디에선가 들려온, 작은 발걸음 소리가 집중을 깨트렸다. 본능적으로 소리를 좇아 고개를 돌리니 자그마한 체구의 시녀가 겁에 질린 얼굴로 서 있는 것이 보였다.

“저, 그게.”

꼭 모아쥔 두 손. 초조한 표정으로 우리를 바라보던 시녀가 개미만한 목소리로 말을 이었다.

“죄, 죄송하지만 신임 성주님께서 언제쯤 이야기가 끝나는지 여쭤보라고 하셔서…….”

빌어먹을 일이다. 이런 일 따위로 집중력이 흐트러지다니.

나도 모르게 눈살이 찌푸려진 그때. 불현듯 섬광 같은 깨달음이 뇌리를 관통했다.

신임 성주. 주원공. 몇 안 남은 황족.

그리고 암천이 이토록 은밀하게 사천 성주를 처리해야만 했었던 이유. 아니, 짐작.

지금 이 순간 떠올린 내 추측이 사실이라면 이건 시작에 불과하다.

성주의 죽음은 암천의 흉계를 알리는 효시(嚆矢)인 동시에, 한 곳을 노린다는 심증을 주기에 충분했다.

‘대국(大國).’

서늘한 한기가 등골을 타고 솟구친다.

눈을 부릅뜬 채 종종걸음으로 멀어지는 시녀를 확인한 나는 간신히 목소리를 쥐어 짜냈다.

“당장 사람을 풀어야 합니다. 사천성주와 주원공에 관련된 것을 모두. 아니, 황제와 그 친인척들까지.”

그리고 동시에, 누군가의 이름이 기억 속 수면 위로 떠올랐다.

방계 황족에 불과한 주원공보다, 아니 천하에 남아 있는 그 어떤 황족보다 천자(天子)라는 이름에 가까운 사람.

더불어 가장 중요한 열쇠가 될 수 있는 사람.

“……주표.”

“뭐?”

“상산왕 주표.”

굳게 닫혀 있는 인벤토리 속에서, 그 작은 아이가 준 증표가 부르르 떨리는 듯했다.
```

## Final English reading copy

```markdown
# Chapter 850

Blood Soul Gu.

The name of the gu poison Namho had identified was ominous enough on its own.

*Not that I’d ever seen a gu poison in person before.*

I muttered to myself and studied the tiny creature writhing in the Divine Physician’s palm.

It was much smaller than a grain of millet, its threadlike body entirely bloodred.

It looked impossible to make out with the naked eye, and it kept struggling to burrow into the Divine Physician’s skin.

As though that were its sole reason for existing.

“If I hadn’t been careful from the start, it would’ve caught me off guard. It’s incredibly strong for something so small.”

Sssk. Ssssk!

As if it understood what he’d said, the Blood Soul Gu struggled even harder, trying to escape. The Divine Physician carefully enclosed it, took out a tiny gourd, and slipped it inside, then sealed the stopper tight.

Only after checking several times for any gaps did he remove the thick leather gloves he’d been wearing.

“Blood Soul Gu. I’ve received countless lessons from my Master over the years, but…to be honest, even I have never seen a gu poison like this.”

Namho nodded at the Divine Physician’s murmur.

“That’s only natural. Blood Soul Gu is a venomous creature scarcely known even in Nanman. More precisely, there can’t be many people left who still remember the name.”

“You mean…”

“It was a very long time ago. Nanman was divided into three rival powers, like a three-legged cauldron, and they were locked in a horrific war. That was when Blood Soul Gu first came to light.”

I couldn’t have been unfamiliar with that story.

I’d heard it several times while staying in Nanman, and if you went back far enough, it was connected to my own sect, the Fire Gate Clan.

It was a story from the past, passed down like a legend through word of mouth and the few records that remained.

And at its center, one sect always appeared.

“…The Five Poisons Sect.”

I murmured the name like a groan, then looked at Namho.

“So Blood Soul Gu originated with the Five Poisons Sect?”

“It happened so long ago that I can’t be certain. But if everything I saw and heard while staying in Nanman is true, Blood Soul Gu was one of the venomous creatures the Five Poisons Sect created after countless attempts.”

“But I never saw anything like this in the Poisonblood Grounds.”

“Gu poisons prefer deep, secluded places. Even if you searched the Poisonblood Grounds as thoroughly as if you were tearing apart a beehive, would this one have been easy to spot?”

He had a point.

The Poisonblood Grounds were crawling with all sorts of bizarre monsters, including the Thousand-Year Spider. In all that chaos, there was no way to identify every creature—including something as hard to see as Blood Soul Gu.

“I’ve heard of the Five Poisons Sect, too. One of the Four Founders of our sect left behind a brief record about Nanman.”

Jeok Cheongang had spoken up without warning. His sunken gaze rested on the gourd holding Blood Soul Gu.

“But that thing is too different from an ordinary gu poison. Its vitality is so tenacious it could survive being pierced through the body with a large needle. And it doesn’t have enough deadly poison to kill its host outright, either.”

“That only makes it more likely to be Blood Soul Gu. Senior Jeok, the gu poisons you’re thinking of cause no trouble as long as the host takes the antidote at regular intervals.”

“That’s what everyone knows.”

“But Blood Soul Gu is different. Ordinary gu poisons are used to threaten and control their hosts. The Five Poisons Sect created that dreadful creature for one reason alone.”

Under everyone’s gaze, Namho let out a breath he’d been holding and finished his thought.

“To kill its host. In a way, it was close to a perfect assassination.”

“……!”

“I spent a long time in Nanman collecting information. I searched through every scrap of what little remained in the records, and sought out the oldest and wisest people from each tribe. I had to feel my way toward the truth in their stories, then sift out whatever might be false.”

One day, after the great war called the Great Faction War had ended, the Martial God vanished without a trace.

Hundreds, even thousands, of sects bound together by every kind of interest and emotion had lost their focal point. Perhaps it was only natural that they began to collapse.

The dissolution of the Murim Alliance.

But the roots of the Hidden Shadow Pavilion remained scattered throughout the world. In a shabby old inn slowly falling apart. On crowded thoroughfares.

And in the remote reaches of Nanman, where venomous creatures and fierce beasts ran rampant.

Namho was one of its deepest and oldest roots.

“The war between the Five Poisons Sect and the Nanman Beast Palace was truly fierce. Sometimes the two sides were evenly matched; at other times, one gained the upper hand.”

The war, they said, had lasted a hundred years. The wells and rivers were poisoned, and the warriors and beasts of the Nanman Beast Palace cut down and tore apart the Five Poisons Sect’s Poison Men.

“All of Nanman was engulfed in poison and flames. If things had continued that way, there would have been no victor or loser—only mutual destruction.”

Namho looked back and forth between Jeok Cheongang and me, then continued.

“Until one day, when an outsider appeared.”

The leader of the Fire Gate Clan, who was traveling the world at the time, received a grand welcome the moment he arrived in Nanman.

A hundred warriors from the Five Poisons Sect welcomed the stranger who dared enter their territory with poison and hidden weapons. That stranger promptly burned everything to the ground, then joined forces with the Nanman Beast Palace.

“With the Fire Gate Sect Leader’s arrival, the tide turned sharply. The Five Poisons Sect must have realized they had nowhere left to retreat. As time passed, they began unleashing things more and more dreadful and vicious.”

When people have lost nearly everything, all that remains is their spite.

The Five Poisons Sect prepared its final counterattack in the deepest reaches of Ailao Mountain, at the Poisonblood Grounds—the most secret and dangerous place of all.

“Near the end of the war, the best warriors of the Nanman Beast Palace began dying one after another. Neither the physicians versed in poison and medicine nor the spiritually gifted priests knew why.”

The Divine Physician, who’d been listening to Namho in silence, spoke with a grim expression.

“They must not have shown any visible injuries.”

“You’re right. It wasn’t poisoning or a plague. The Nanman Beast Palace realized what was causing it only after the number of dead warriors passed a hundred.”

“Even if Blood Soul Gu was so small and stealthy that it was difficult to find, surely they could have discovered it sooner once so many people had died.”

“I thought so, too. But it seems there was a good reason.”

Namho shook his head slightly and continued.

“Everyone was exhausted from the hundred-year war. The word ‘peace’ had long since lost its meaning, and death was seen as a form of rest. In those circumstances, it might have seemed only natural that some warriors were afflicted with madness.”

“Madness…?”

“That’s right. They said most of them would act like they’d lost their minds one day, then fight more bravely than anyone the next.”

The Divine Physician murmured as if sighing.

“City Lord. That was exactly how the City Lord behaved. When I first heard about it, I thought it was a mental illness brought on by losing his beloved concubine.”

“Blood Soul Gu grows stronger when its host’s mental strength weakens, so the two are likely connected.”

“Then how did the Nanman Beast Palace learn the truth?”

“They said the information came from interrogating an Elder of the Five Poisons Sect after capturing him. At first, it wandered through the duodenum and the acupoints, using mild poison to cause auditory and visual hallucinations. In the end, it gradually ate away at the brain and drove its host to death.”

“……!”

“Each warrior died at a different time. Some held out for as little as six months; others lasted several years.”

“So they only begin to act once their host’s body and mind grow weak.”

“That’s right. But their killing power and the time they took fell far short of what the Five Poisons Sect had originally wanted. Perhaps that’s why they managed to improve so few specimens before the sect was destroyed. That’s everything I’ve learned.”

After Namho finished, a heavy silence fell.

No one spoke, but it wasn’t hard to imagine what the others were thinking.

A great war that had drenched Nanman in blood for more than a hundred years.

And now, after all those years, Blood Soul Gu had appeared once more—in the body of a government official from the Great Nation, someone who wasn’t even a martial artist.

I closed my eyes and muttered to myself.

No. The two characters had been circling in my mind ever since I learned Blood Soul Gu came from Nanman. I finally said them aloud.

“Dark Heaven.”

The darkness before my eyes cleared. When I opened them, I saw three faces looking at me beneath the soft light of the night-shining pearls.

“Blood Soul Gu was almost forgotten in Nanman. The only way it could have made its way to the Central Plains is if they brought it here. This is definitely their doing.”

Jeok Cheongang spoke in a low voice.

“The Southern Heaven Demon Empress.”

“It’s been decades. Dark Heaven set foot in Nanman and waited for its moment in the Poisonblood Grounds. They had more than enough time to find Blood Soul Gu.”

“More than enough. No, plenty.”

Jeok Cheongang nodded slightly, then asked,

“But why would they harm this man?”

“That…”

My voice trailed off as I looked down at the City Lord of Sichuan Province’s corpse.

His arms and legs were cold. His face was as white as paper, with no trace of pain.

Yes. Jeok Cheongang’s question was the key.

Why had they killed this man? Why use such a secretive method?

He’d held the high office of City Lord, but that was all.

A corrupt, moderately greedy official, the kind you could find anywhere.

If Dark Heaven wanted, they could take his life as easily as pulling a coin from their pocket.

*So why go to all this trouble?*

Was it because the City Lord had mobilized the government troops to help us during the Sichuan Blood Tragedy?

The thought crossed my mind, but I shook my head.

No. If they wanted to retaliate, a far more horrific death would have been a hundred times better.

Even if he was a high-ranking official like the City Lord, they could make sure the whole world knew that no one should dare stand against Dark Heaven again.

Even those who thought themselves separate from Murim would have reason to fear them.

*But if they chose this method anyway…*

There was something else. Some still-unknown goal that Dark Heaven truly wanted to achieve.

And just as my thoughts, one after another, reached that point—

Tap.

A faint footstep from somewhere broke my concentration. I instinctively turned toward the sound and saw a small maid standing there, her face full of fear.

“Um, well…”

Her hands were clasped tightly together. She looked at us anxiously and continued in a voice barely louder than a whisper.

“I-I’m sorry, but the new City Lord asked me to find out when you’d be finished talking…”

Damn it. How could something as trivial as that ruin my concentration?

I frowned without meaning to. Then a flash of insight suddenly shot through my mind.

The new City Lord. Ju Wongong. One of the few remaining members of the imperial family.

And the reason Dark Heaven had needed to deal with the City Lord of Sichuan so secretly. No—the suspicion.

If my hunch was right, this was only the beginning.

The City Lord’s death was a signal of Dark Heaven’s sinister scheme—and enough to make me suspect they were targeting one place.

*The Great Nation.*

A chill ran up my spine.

I watched the maid hurry away, then managed to force the words out.

“We need to send people out immediately. Find out everything about the City Lord of Sichuan and Ju Wongong. No—the Emperor and all his relatives, too.”

At the same time, someone’s name rose to the surface of my memory.

Someone closer to the title of Son of Heaven than Ju Wongong, a distant member of the imperial family—or any other royal left in the world.

And someone who could be the most important key of all.

“…Zhu Bao.”

“What?”

“Prince Shangshan. Zhu Bao.”

Inside my firmly shut Inventory, the token that little boy had given me seemed to tremble.
```
