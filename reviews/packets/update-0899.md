<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0899.txt",
      "sha256": "8b1b64fd626b03dbbc37784239571ae3a8b9615f4c2a6f4925fe3b87cd6df240",
      "bytes": 12972
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a6e43a219f417a06ca93fa3c90d9a5a42ab6a5aca8a7e5155ccab80a522c937b",
      "bytes": 1561
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "25f29bd53ba3edcd9a03b3f0adf18d029dedffaf0a6925e39ad1e11a2efb2804",
      "bytes": 230838
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2764658ac90d2bef597fc6b6b74367b6b2d55fdd8206fcd6f89839b604cb8b34",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "cf0e8e99140b716b09c85693ec23cf9d544040bbe5b41900f9d06d4f65fd2e2a",
      "bytes": 837
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c6b5e8741e355804c680d79e26d7f1f2dfcddac953033875c3facb77b0e1d317",
      "bytes": 1369
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ebbbab7813a5850da88f9ad9e24c46ca9771becf98852b62e64eaf84d92da52e",
      "bytes": 622
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "d7912500fd5b47e801f382f320dea8d9afc8c1ad08fcd1d8b8708861ec0b3aa1",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ead4207b37bea0c8bdc317b844fae2124946506bd434491dd7489b0ce8d1c7b",
      "bytes": 261385
    }
  ],
  "estimated_tokens": 9853
}
-->

# Durable State Update — Chapter 899

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
1 and safe_through 899. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 899. Profile updates may replace only one
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
  "chapter": 899,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 899,
    "continuity_sources": [899],
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
    "The Emperor’s three-day birthday banquet for the imperial prince is underway; Taekyung and Hong Jin are being escorted to the Grand Banquet Hall.",
    "Public anger over the Emperor’s response to the flood is growing.",
    "Ma suspects the Emperor has allied with Dark Heaven and that Baek Yeon and So Gyo are connected to it; these allegations remain unconfirmed.",
    "Taekyung sent Hyuk Mujin and the rest of the Fire Dragon Pavilion, except Taekyung and his master, to await Murim Alliance reinforcements expected within half a day to a day.",
    "Mujin carries Taekyung’s note and must confirm they are not being followed before checking its destination.",
    "Taekyung and Jeok may have to risk their lives in the coming gamble; Taekyung has resolved to proceed."
  ],
  "continuity_sources": [
    897,
    898
  ],
  "open_questions": [
    "Will the Murim Alliance reinforcements arrive as expected, and who will be among them?",
    "What destination is written on Taekyung’s note, and what awaits the group there?",
    "Are Ma’s suspicions about the Emperor, Baek Yeon, and So Gyo’s ties to Dark Heaven correct?",
    "Who was the bamboo-hat man, and what were his intentions?"
  ],
  "safe_through": 898,
  "temporary_decisions": [
    "Use “Twelve Palaces of the Zodiac” for 黃道十二宮.",
    "Use “Seal-Holding Eunuch of the East Depot” for 東廠掌印太監.",
    "Keep “Shangshan” in the crowd’s mountain imagery where it alludes to Prince Shangshan."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 무인     | **martial artist**                               | Default term                                          |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 양귀 | **Yang Ghost** | Shortened counterpart to the established Yin Ghost. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 896
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 898
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 896
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, and Jin has signed its pledge and arranged for Ma to summon Murim Alliance reinforcements.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 896
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 896
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃899화



주위가 온통 황금빛으로 번쩍거려서 그런지, 나는 잠시나마 천하제일의 거부가 된 듯한 기분에 사로잡혔다.

슬프게도 현실과는 크나큰 괴리감이 있었지만.

철컥, 철컥.

아마 저 살벌한 금속음만 없었다면 조금 더 몰입할 수 있었을 거다.

하지만 나와 홍진을 에워싼 채 걸음을 옮기는 금의위들에게서 는 그런 배려심은 찾아볼 수 없었다.

‘사실 배려를 바라는 게 미친놈이긴 하지.’

나도 모르게 흘러나온 실소와 함께 옆에서 뜨거운 시선이 느껴진다. 홍진이 어이없다는 눈빛으로 이쪽을 빤히 바라보고 있었다.

“왜요?”

“……이건 혹시나 해서 물어보는 건데, 지금 쳐다보는 이유를 모르는 건 아니죠?”

“음. 이런 상황에서 갑자기 웃어서?”

“다행이네. 난 또 진 공자가 완전히 정신이 나간 줄 알았지 뭐야.”

“염려 마세요. 정신 줄 꽉 붙들어 매고 있으니까.”

이런 백척간두의 상황에서 정신 나간 놈처럼 허허 웃고 있을 수만은 없지 않겠나.

벼랑 끝에 몰리면 오히려 마음이 차분해지는 법이다.

머릿속의 모든 것이 지워지고, 오직 생존이라는 단어 하나만 오롯이 남아 있게 되는 것이다.

바로 지금의 나처럼.

“그 말, 믿을게요. 믿을 수밖에 없으니까.”

혼잣말처럼 뇌까린 홍진이 아직 꺼지지 않은 곰방대를 느릿느릿 빨아들였다.

후욱, 벌겋게 타오르는 불씨와 함께 뿜어진 새하얀 연기가 금의위들 사이로 흩어진다.

황궁 내에서, 그것도 곧 목이 날아갈지도 모르는 위기를 앞에 두고 저 당당한 길빵이라니.

홍진의 배짱에 내심 감탄하고 있던 그때, 불현듯 파르르 떨리는 그의 속눈썹과 나른함에 젖어 가는 얼굴이 보였다.

후각에 와닿는 연기의 독특한 향기까지도.

‘생각해 보면, 홍진의 근처에만 가면 항상 저 냄새가 풍겼지.’

평소에는 그러려니 했다.

내가 무슨 금연 홍보대사도 아닌데 홍진이 곰방대 좀 물고 있다고 한들 이상할 것도, 만류할 이유도 없었으니까.

그저 남자로서 지녀야 할 물건이 없으니 니코틴이라도 빵빵하게 채우는구나, 하고 단순하게 생각했을 뿐이다.

하지만 그 와중에도 묘한 기시감을 느낀 적이 있었다.

그 기시감의 정체는 왠지 모를 익숙함이었고, 나는 어렵지 않게 그날의 기억을 떠올릴 수 있었다.

‘그래, 황제를 알현하고 돌아온 직후. 바로 그날이었어.’

동시에 머릿속을 번뜩 스쳐 지나가는 어떤 생각.

나는 천천히 연기를 뿜어내고 있던 홍진을 물끄러미 바다보다, 불쑥 입을 열었다.

“생각보다 맛이 괜찮나 보네요. 냄새만 맡았을 때는 영 아닌 것 같았는데.”

“그게 무슨. 아, 이거?”

내가 조용히 고개를 끄덕이자, 홍진이 손에 쥔 곰방대를 가볍게 흔들었다.

“맛이랄 것까지야. 그냥…… 일종의 습관인 거죠. 그것도 아주 질이 나쁜.”

물론 흡연이 몸에 안 좋은 것은 사실이다.

적어도 현대의 기준에서는.

‘하지만 이 시대상으로는 딱히 배척받는 행위는 아니었을 텐데.’

이곳은 21세기까지 전해져 내려오는 역사 어디에도 기록되지 않은 세상이지만, 여러 부분에서 상당히 흡사하다. 각 지방의 지명, 복색과 음식, 마지막으로 사람들의 인식까지도.

그리고 그런 의미에서 보자면, 흡연은 딱히 질이 나쁘다고 할 만한 일은 아니었다. 아니, 오히려 온갖 향락을 즐기는 높으신 분들의 주장으로 흡연이 장려되기까지 했다. 그나마도 담뱃잎이 비싸서 어지간한 양민들에게는 호사였지만.

‘그런데 바로 그 높으신 분인 홍진이 저렇게까지 말한다고?’

바로 촉이 온다.

뭔가 있다. 아직 내가 알아내지 못한 무언가가.

나는 홍진을 향해 손을 내밀었다.

“제가 한번 피워 봐도 됩니까?”

“응? 피우겠다고요? 이걸?”

“네. 그냥 이참에 한 번쯤은 경험해 보고 싶어서요.”

대답과 동시에 시선을 마주친 그 짧은 순간, 홍진의 눈썹이 아무도 눈치채지 못할 만큼 미미하게 들썩였다.

그리고 그건 의중을 정확히 파악했다는 신호이기도 했다.

“희한하네. 내가 아는 무인들은 술은 곧잘 마셔도 앵속(罌粟)은 잘 안 하던데.”

“앵속이라면…….”

“양귀비의 진액을 모아 말린 거죠. 간혹 심경이 복잡할 때 피우면 머릿속이 차분해지고 뭔가 나른해지는데, 보통은 고통을 덜어 주기 위한 용도로 많이 쓰이지만 중독성이 강해서…….”

홍진의 뒷말이 메아리처럼 멀게 느껴진다.

내 머릿속에는 이미 한 단어만이 둥둥 떠다니고 있었다.

‘아편!’

제아무리 학교 수업을 수면 보충쯤으로 생각했던 나지만, 그래도 최소한의 상식 정도는 주입되어 있다.

특히나 열정적이었던 세계사 선생님의 걸걸한 목소리는 왔던 잠마저 달아나게 하는 마력이 있었다.



‘마! 진태경!’

‘흡. 에?’

‘너 인마. 지금 막 쌤이 뭐라고 했어. 눈깔 굴리지 말고 딱 말해.’

‘어. 그러니까 그게…….’

‘그렇지. 모르겠지. 니는 모를 수밖에 없지. 뒤에서 3교시 내내 처자고 있으니 이건 뭐, 호텔인지 학교인지…….’

‘아, 기억났는데요.’

‘뭐? 기억이 나? 그래, 꿈속에서 뭔 창의적인 개소리를 듣고 왔나 물어나 보자. 뭔데?’

‘마 진태경이요.’

‘…….’

‘아니……에요?’

‘아니, 맞는데. 맞긴 한데…… 하. 임마 이거 진짜 도라이네. 아편 전쟁! 아편 전쟁 얘기하고 있었는데 진짜 와, 돌아 뿌겠네. 따라 해라. 아편 전쟁!’

‘예? 아청 전쟁이요?’

‘아청…… 야, 반장아. 김민정이.’

‘네?’

‘지금 바로 경찰 불러라. 그냥 내 오늘 점마 조지고 폭력 교사로 잡혀 들어갈란다.’



다행히 경찰이 출동하는 불상사는 벌어지지 않았고, 나는 울분에 찬 샤우팅을 들은 직후 아편 전쟁에 관한 단락을 깜지로 써 가는 형벌을 받았다.

그리고 그 결과 흰 피부의 섬나라 짱깨가 진또배기 대륙 짱깨를 침략했다는 사실을 비롯한 각종 사소한 정보를 돌대가리 속에 집어넣을 수 있었다.

이를테면, 아편의 원료가 양귀비라 불리는 식물이라는 것도.

‘이게 이럴 때 도움이 되네.’

나는 그 시절, 누구보다 열정적이었던 세계사 선생님에게 내심 감사의 뜻을 표했다.

덕분에 새로운 정보를 하나 더 알아낼 수 있었으니까.

‘아편. 아니 앵속의 그 독특한 향…… 이미 맡아 본 적이 있어. 홍진의 것보다도 더욱 진하게.’

불과 며칠 전.

나는 분명 기시감을 느꼈었고, 지금에 이르러서야 무심코 지나쳤던 그 기시감의 정체를 깨달았다.

- 조용히 들으세요. 그 어떤 반응도 하지 말고.

아무 일도 없다는 듯 계속해서 묵묵히 걸음을 옮기는 홍진을 향해, 나는 입술을 달싹여 전음(傳音)을 흘려보냈다.

- 만약, 황제가 앵속을 한다면 무슨 이유 때문일 것 같습니까?

그날. 그 시간. 그 순간.

내가 느꼈던 기시감의 첫 근원지는, 건청궁에서 맞닥트린 만인지상(萬人之上)의 존재였다.



* * *



허.

가쁜 날숨과 함께, 사내는 불현듯 눈을 떴다.

어둠 너머로 은은하게 일렁이는 횃불과, 길게 드리운 형형색색의 얇은 비단이 가장 먼저 그의 시야를 채웠다.

‘이곳은…….’

모를 수가 없는 곳이다. 그가 지난 십여 년의 세월 중 대부분을 보냈던 침소이자 요새였으니까.

한동안 식은땀에 젖은 채 숨을 고르던 사내는 문득 입을 열었다.

“게 누구 없느냐.”

메마른 목소리가 울려 퍼진 그 순간.

스륵.

어디선가 불어온 바람이 비단을 흔들었다. 그 사이를 파고든 한 줄기 전음이 사내의 귓가에 닿았다.

- 분부하십시오.

사내는 한동안 말없이 자신의 얼굴을 쓸어내렸다.

나이와는 맞지 않는 깊게 팬 주름살 사이로 피로의 흔적이 느껴진다.

깨어난 지 어느 정도의 시간이 흘렀음에도 가슴은 아직 세차게 두방망이질 치고 있었다.

“이미 해가 진 듯하구나.”

- 곧 술시(戌時)입니다.

“술시라, 하면 대연회는?”

- 예고했던 미시가 훌쩍 지나, 문무백관이 모두 모여 있는 상태입니다.

“그럼 그자도?”

그자.

대연회를 위해 모인 수많은 이들 중 어느 한 사람을 가리키기에는 퍽 모자란 지칭이었으나, 어둠 속 그림자는 망설임 없이 대답했다.

- 예.

“……의외로군. 제아무리 강호인들이 물불 안 가리는 이들이라고는 해도, 이건 터무니없을 만큼 무모해.”

혼잣말처럼 뇌까린 황제가 말을 이었다.

“하지만 누군가는 이미 예견했던 일이기도 하지. 그렇다면 그자의 스승도 남았겠군.”

- 그 역시 자리에 참석하였습니다. 하온데…….

“계속하게.”

- 두 명을 제외한 다른 무림인들이 황궁을 이탈했습니다.

“이탈?”

- 그렇습니다. 파악하기로는 어떤 목적을 갖고 움직이는 듯했는데, 더 이상 추적하지 못했습니다.

“추적하지 못했다고?”

사내는 미간을 좁혔지만, 뒤이어 이어진 그림자의 한 마디에 입을 다물 수밖에 없었다.

- 예. ‘그녀’가 직접 나서서 제지했습니다.

“……음.”

- 명하신다면 지금이라도 당장.

“아니, 아니다.”

고개를 내저은 사내는 천천히 자리에서 일어났다.

한 사람을 위한 침소라고 하기에는 너무나도 광활한 그 공간에서, 그는 황금빛 수실로 아로새겨진 침의(寢衣)를 걸친 채 커다란 거울 앞에 섰다.

스륵. 툭.

부드러운 비단이 살을 스치며 바닥을 나뒹군다.

평범한 이들이라면 찰나에 엄습하는 한기(寒氣)에 몸을 떨었을 것이나, 홀로 우뚝 선 사내는 철탑처럼 굳건했다.

대군을 이끌고 반란군을 휩쓸던 그때처럼.

십여 년 전의 그 날처럼.

그러나 여전한 기개와는 반대로, 스스로를 비춘 거울 속의 모습에서 과거의 모습은 쉽게 찾아볼 수 없었다.

‘늙었군. 몰라볼 정도로.’

사내는 마음속으로 뇌까렸지만, 그 안에 후회의 감정은 없었다.

지금까지 걸어온 길은 누군가는 반드시 해야 할 일이었다.

다만 그가 선택받았을 뿐이다.

누구도 감히 고개 들어 쳐다보지 못할 만큼 눈부신 용포(龍袍)를 걸치고, 천자(天子)라는 두 글자를 허락받았을 뿐이다.

후회는 없었다.

불과 한 걸음밖에 남지 않은, 앞으로 가야 할 길만 남아있을 뿐.

“이제, 건청궁을 나서야겠다.”

그 한 마디에 그림자가 녹아든 어둠이 일렁였고, 쥐 죽은 듯이 고요하던 건청궁이 깨어났다.

아니, 그들은 처음부터 준비되어 있었다.

사내를, 황제의 명령에 따라 죽고 죽일 모든 준비가.

그리고 활화산처럼 맥동하는 건청궁의 지붕 위에서, 흐린 하늘을 바라보는 한 여인이 있었다.

“오늘도 비가 오려나.”

소교(小嬌)는 양 옆구리에 매달린 애병을 매만졌다.

오랜만에 되찾은 그것은 얼음처럼 차가웠고, 그 안에 담긴 기운은 불처럼 뜨겁게 끓어오르고 있었다.



* * *



대연회장은 믿을 수 없을 만큼 광활했고, 이해할 수 없을 만큼 고요했다. 수많은 대소신료가 한자리에 모여 있음에도 그 누구도 입을 열지 않았다.

적어도 지금 이 순간만큼은 그들 모두가 장님이자 소경이었고, 말 못 하는 벙어리였다.

이미 모든 상황을 아는 이들은 조용히 지금까지의 삶을 반추(反芻)했으며, 모르는 이들은 대연회장을 잠식한 이 숨 막히는 기운 앞에서 옴짝달싹하지 못했다.

누가 먼저 입을 열 것인가.

누가 먼저…… 칼을 뽑을 것인가.

모두가 같은 생각을 떠올린 그때.

“저기 오네.”

정적을 깨트리는 목소리가 있었다.

“다섯 시간 지각. 이거 맞냐?”

진태경의 시선 끝은, 일렁이는 횃불 뒤로 펼쳐진 어둠을 꿰뚫고 있었다.

정확히는 그 너머에서 한 마리의 용처럼 다가오는, 거대한 황금빛 행렬을.
```

## Final English reading copy

```markdown
# Chapter 899

Maybe it was because everything around me was gleaming gold, but for a moment I felt like the richest man in the world.

Sadly, reality was a long way from that.

Clank. Clank.

I might’ve been able to immerse myself a little more if not for those ominous metallic sounds.

But the Embroidered Uniform Guards surrounding Hong Jin and me as they marched along showed no sign of offering that kind of consideration.

*To be fair, it’d be crazy to expect consideration from them.*

A laugh slipped out before I could stop it. I felt a heated gaze from beside me. Hong Jin was staring at me, looking baffled.

“What is it?”

“……I’m only asking just in case, but you do know why I’m looking at you, right?”

“Hmm. Because I suddenly laughed in a situation like this?”

“Thank goodness. I thought Young Master Jin had completely lost his mind.”

“Don’t worry. I’m holding on to my sanity.”

It wasn’t as if I could just stand there grinning like a lunatic with my life hanging by a thread.

When you’re backed up against a cliff, your mind actually grows calmer.

Everything gets wiped away, leaving only one word behind: survival.

Just like right now.

“I’ll take your word for it. I have no choice.”

Hong Jin muttered as if to himself, then slowly drew on his still-lit long-stemmed tobacco pipe.

Whoosh. A stream of white smoke billowed out with the glowing ember and drifted among the guards.

Smoking so boldly inside the imperial palace, with his head possibly about to roll any moment now. I was privately impressed by Hong Jin’s nerve when I caught sight of his eyelashes trembling and his face growing languid.

Even the distinctive fragrance of the smoke reached my nose.

*Now that I think about it, I always smell that whenever I’m near Hong Jin.*

Normally, I’d thought nothing of it.

I wasn’t some anti-smoking spokesperson. There was nothing strange about Hong Jin puffing on a pipe, and no reason for me to stop him.

I’d simply assumed he was filling up on nicotine since he was missing something a man ought to have.

But even so, I’d occasionally felt a strange sense of déjà vu.

There was something familiar about it, and I had no trouble remembering when I’d felt that way before.

*Right. Immediately after I returned from my audience with the Emperor. That very day.*

At the same time, an idea flashed through my mind.

I gazed at Hong Jin as he slowly exhaled smoke, then spoke up.

“It seems to taste better than I expected. It didn’t smell like much when I caught a whiff.”

“What are you talking about? Oh, this?”

When I gave a quiet nod, Hong Jin lightly waved the pipe in his hand.

“I wouldn’t say it tastes good. It’s just… a kind of habit. A very bad one, too.”

Of course smoking was bad for your health.

At least by modern standards.

*But in this era, it wasn’t exactly frowned upon.*

This world had no place in any history that made it down to the twenty-first century, but it was remarkably similar in many ways. The names of its regions, the clothes and food, and even people’s attitudes.

And in that sense, smoking wasn’t something you’d call a bad habit. If anything, it was encouraged by the claims of the powerful, who indulged in all manner of pleasures. Tobacco leaves were expensive, though, so it was a luxury most commoners could hardly afford.

*But Hong Jin, one of those powerful people himself, calls it a bad habit?*

That set off alarm bells.

There was something to it. Something I hadn’t figured out yet.

I held out my hand to Hong Jin.

“Can I try it?”

“Hmm? You want to smoke? This?”

“Yes. I thought I’d give it a try while I had the chance.”

In the brief moment our eyes met after I answered, Hong Jin’s eyebrow twitched so slightly that no one else could have noticed.

It was also a sign that he’d understood exactly what I meant.

“How curious. The martial artists I know drink readily enough, but they rarely touch poppy.”

“Poppy…?”

“It’s the dried sap of the poppy. If you smoke it when your mind is troubled, sometimes it calms you down and makes you feel drowsy. It’s often used to relieve pain, but it’s highly addictive, so—”

Hong Jin’s words drifted away, like an echo.

Only one word was floating through my mind.

*Opium!*

I might’ve treated school lessons as extra time to catch up on sleep, but at least a little basic knowledge had managed to stick.

Especially since my world history teacher had a booming voice so passionate it could chase away the sleep that had already claimed me.

*“Hey! Jin Taekyung!”*

*“Hrk. Huh?”*

*“You punk. What did the teacher just say? Don’t roll your eyes around—tell me.”*

*“Uh, well…”*

*“Right. You don’t know. Of course you don’t. You’ve been sleeping through three whole periods back there, so at this point, I can’t tell if this is a hotel or a school…”*

*“Oh, I remember now.”*

*“What? You remember? Fine, let’s hear what kind of creative bullshit you picked up in your dream. What is it?”*

*“Hey, Jin Taekyung.”*

*“……”*

*“No…?”*

*“No, you’re right. You are. But… Jesus, you’re a real nutcase. The Opium War! We were talking about the Opium War. You’ve got to be kidding me. Repeat after me. The Opium War!”*

*“What? The Youth Protection War?[^1]”*

*“Youth Protection… Hey, class president! Kim Minjeong!”*

*“Yes?”*

*“Call the cops right now. I’m going to beat this punk and get arrested for assaulting a student.”*

[^1]: Taekyung mishears *apyeon* (opium) as *acheong*, shorthand associated with Korea’s law protecting children and youth from sexual crimes.

Fortunately, it never came to the police getting called. Right after I got an earful of my teacher’s furious shouting, I was sentenced to write out a whole section on the Opium War by hand.

As a result, I managed to cram all sorts of trivial details into my thick skull—including the fact that the white-skinned island chinks invaded the genuine mainland chinks.

For instance, that opium came from a plant called the poppy.

*So that’s useful now.*

I silently thanked my world history teacher, who’d been more passionate than anyone.

Thanks to him, I’d just learned something new.

*Opium. No, that distinctive scent of poppy… I’ve smelled it before. Stronger than Hong Jin’s.*

Just a few days ago.

I’d definitely felt that déjà vu. And only now did I realize what I’d overlooked at the time.

*Listen carefully. Don’t react in any way.*

Still walking along as if nothing had happened, Hong Jin received a Sound Transmission from me as my lips barely moved.

*If the Emperor smokes opium, what do you think the reason might be?*

That day. That time. That moment.

The first source of the déjà vu I’d felt had been the one above all others, whom I’d encountered at Qianqing Palace.

* * *

“Hah.”

With a ragged exhale, the man suddenly opened his eyes.

The first things to fill his view were the torchlight flickering faintly beyond the darkness and the long, colorful silk curtains hanging around him.

*Where am I…*

There was no way he could mistake it. This was his bedchamber and fortress, where he’d spent most of the past decade or so.

The man lay there for a while, soaked in cold sweat as he caught his breath. Then he suddenly spoke.

“Is anyone there?”

The dry sound of his voice had barely faded when—

Rustle.

A breeze from somewhere stirred the silk curtains. A thread of Sound Transmission slipped through them and reached his ear.

*—At your command.*

The man said nothing for a while, slowly running a hand over his face.

He could feel the signs of fatigue in the deep furrows that didn’t belong on a face his age.

Though some time had passed since he’d awoken, his heart still pounded fiercely.

“It seems the sun has already set.”

*—It will soon be the hour of the Dog.*

“The hour of the Dog, you say. And the grand banquet?”

*—The appointed hour of the Goat has long since passed. The civil and military officials have all gathered.*

“Then is he there, too?”

He.

It was an inadequate way to refer to just one person among the many gathered for the grand banquet. Yet the shadow in the darkness answered without hesitation.

*—Yes.*

“……Unexpected. The martial artists of the world may be reckless enough to rush headlong into anything, but this is absurdly reckless.”

The Emperor muttered as if to himself, then continued.

“But someone had already foreseen this. In that case, his Master must still be there, too.”

*—He has attended as well. However…*

“Go on.”

*—The other martial artists, except for the two of them, have left the imperial palace.*

“Left?”

*—Yes. From what we’ve learned, they seem to be moving with a purpose, but we could not follow them any farther.*

“You couldn’t follow them?”

The man frowned, but the shadow’s next words left him with no choice but to fall silent.

*—Yes. ‘She’ personally intervened and stopped us.*

“……I see.”

*—If you command it, we can act at once.*

“No. No.”

The man shook his head and slowly rose from his bed.

The room was far too vast to be a bedchamber for one person. He stood before a large mirror, dressed in sleeping robes embroidered with golden thread.

Rustle. Thud.

The soft silk slid over his skin and fell to the floor.

An ordinary person would have shivered at the sudden chill. But the man standing alone was as solid as an iron tower.

Just as he’d been when he led a great army to crush the rebels.

Just as he’d been that day, more than a decade ago.

But for all his enduring spirit, the figure reflected in the mirror bore little resemblance to the man he’d once been.

*I’ve aged. Beyond recognition.*

The man thought to himself, but he felt no regret.

The path he’d walked was one someone had to take.

He’d simply been the one chosen.

He’d donned a dragon robe so dazzling no one dared look up at him, and been granted the two characters of Son of Heaven.

He had no regrets.

There was only the path still ahead, with just one step left to go.

“It’s time for me to leave Qianqing Palace.”

At his words, the darkness where the shadow had melted stirred, and Qianqing Palace, silent as a grave, sprang to life.

No. They had been ready from the very beginning.

Ready to kill and die at the Emperor’s command.

And on the roof of Qianqing Palace, its pulse throbbing like a volcano on the verge of eruption, a woman gazed up at the cloudy sky.

“Will it rain again today?”

So Gyo stroked the weapons hanging at either side of her waist.

She’d reclaimed them after a long time. They were as cold as ice, and the energy within them boiled as hot as fire.

* * *

The Grand Banquet Hall was unbelievably vast and impossibly quiet. Countless officials, great and small, had gathered in one place, yet not a single one of them spoke.

At least for that moment, they were all blind and sightless, all mute and unable to speak.

Those who already knew what was happening quietly reflected on the lives they’d led up to then. Those who didn’t know were frozen in place by the suffocating presence that had swallowed the Grand Banquet Hall.

Who would speak first?

Who would be the first to… draw a sword?

Just as everyone was thinking the same thing—

“There he is.”

A voice broke the silence.

“Five hours late. Are you kidding me?”

Jin Taekyung’s gaze pierced the darkness beyond the flickering torches.

More precisely, it pierced the enormous golden procession approaching from beyond, like a dragon.
```
