<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0076.txt",
      "sha256": "d4705e72d7a430e03be1c80b40d29bccb692fdfaae58b317dd4be0978ecfd093",
      "bytes": 13389
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "52ce5e86936da170336569c92a045c0570638095ef294cb6a9e2fc881b2b12c4",
      "bytes": 5307
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5fe35945ca7b3113f89db34ca78aad82c70c6ed05f781bb48ac53667151a6fd0",
      "bytes": 4214
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "70d1e2c2294e7317a2ebbdb1ba7d61c482001759a17e8f23fa85bdf54c4244e7",
      "bytes": 1541
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2c4e645b01ee0ac4881512abdf96178d983a82513c008ac83294bbb982f5b143",
      "bytes": 3859
    }
  ],
  "estimated_tokens": 11112
}
-->

# Durable State Update — Chapter 76

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 76. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 76. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 76,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 76,
    "continuity_sources": [76],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and he states that ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy. Circulating his qi slightly increases his internal energy, and Sleep Mode normally keeps his sleep below three hours except when he is seriously injured.",
    "Seong Jinho is thirty, has lived with Taekyung as a friend and brother for years, and now plans to move out of the goshiwon soon, though the date is not fixed.",
    "Team Leader Choi owns the café where he meets Taekyung and gives him a contract; Taekyung signs it, after which a System alert appears.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique; the Training? Trial! Quest succeeded and granted a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured and under treatment after the attack; the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training. Jin Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visited Song Sword Sect, and delivered Wikyung's summons as both summons and warning; Wikyung found no information on Dark Heaven in the family records.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months. Soyul is five and does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout. Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect. Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day; its completion and Reward remain unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin departed for Eung-hyeon in a four-horse carriage because Lee Seowol requested their visit and Mukyung may learn Peak martial arts."
  ],
  "continuity_sources": [
    75
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "The contents and consequences of the contract Taekyung signed with Team Leader Choi, and the System alert that followed, remain unknown."
  ],
  "safe_through": 75,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, Martial Artist Jang for 장 무인, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, and 일각 as fifteen minutes.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, seventh-tier student for 내신 칠 등급, Team Leader Choi for 최 팀장, Designer-Brand Junkie for 명품충, and Qi Sense for 기감."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |

## Exact glossary matches

| 무림     | **Murim**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 산서     | **Shanxi**             |
| 임꺽정 | **Im Kkeokjeong** |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 45
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran member of the Peace Guild’s Gate party
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother and recommends him to Team Leader Choi

## Korean source

```text
＃76화



띠링.



- 길드, [평화]에 가입했습니다!

- 업적, [길드 가입]을 완료했습니다!

- 업적 달성 보상으로 10포인트를 획득합니다.



‘이것도 업적이야?’

지금 같은 시스템 메시지가 뜰 때마다 뭔가 영웅이 된 것 같다. 업적 달성이라니. 돈 벌려고 길드 가입한 것치고는 제법 거창한 포장이다.

‘뭐, 나야 좋지만.’

10포인트만 해도 짭짤한 보상인데, 뒤를 이은 최 팀장의 말을 들은 후에는 자꾸만 솟구치는 입꼬리를 억눌러야 했다.

“계약금은 오늘 안에 처리될 겁니다. 그밖에 거주지 문제나 다른 사안들은…….”

계약금 5억, 월 5천만 원의 고정 급여와 7할의 정산 비율.

길드에서 제공하는 집과 차, 여타 수십 가지 사항들까지.

이미 계약서로 몇 번씩 확인한 내용이지만 이렇게 들으니 감회가 새롭다.

‘나, 용 됐구나.’

불과 세 달 전까지만 하더라도 내 인생이 이렇게 풀릴 거라고는 상상도 못 했다.

무림에서는 산서잠룡, 현실에서는 억대 연봉을 우습게 벌어들이는 헌터가 되다니.

“팀장님.”

“장비 대여 같은 경우는 제 컬렉션을 제외하고 얼마든지…… 예?”

“저 뺨 한 대만 때려 주세요. 꿈이면 빨리 깨게.”

말이 끝나기가 무섭게 눈앞이 번쩍했다.

퍽!

‘짝!’이 아니라 퍽?

나는 얼얼한 턱을 만지며 중얼거렸다.

“진짜 사양 않고 때리시네.”

“부탁을 거절 못 하는 성격이라.”

“주먹 쓰라는 말은 안 한 것 같은데.”

“안 쓰라는 말도 안 하셔서.”

“…….”

새로 생긴 [맷집] 능력치가 아니었으면 볼썽사납게 나동그라질 뻔했다.

‘맞다. 이 인간 B급 헌터였지.’

준비 자세도 없이 뻗어 낸 주먹이 턱에 정확히 꽂혔다. 힘과 타격점. 완벽하다.

“그래도 보통은 따귀 아닙니까?”

“예외도 있죠. 어때요, 정신은 좀 드십니까?”

“……아주 확 드네요.”

“그거 잘됐네요. 기왕이면 맨정신일 때 만나는 게 첫인상에 좋지 않겠습니까?”

최 팀장의 뜬금없는 말에 내가 되물었다.

“첫인상? 누구 만나러 가요?”

“누구겠습니까.”

최 팀장이 웃으며 말을 이었다.

“다른 길드원들이죠.”

“아.”

그제야 잊고 있던 사실 하나가 떠올랐다.

길드를 창설하기 위해서는 최소 세 명의 인원이 필요하다는 것을.

“그럼 슬슬 출발할까요.”

최 팀장이 창밖을 가리켰다. 카페 앞 주차장으로 매끈하게 빠진 검은색 리무진이 미끄러져 들어오는 중이었다.



* * *



“축하드립니다.”

커피 CF에 등장할 법한 중후한 목소리의 주인공은 김 집사였다. 무더운 여름에도 정장을 차려입은 그는 능숙한 솜씨로 리무진을 운전하는 중이었다.

“아, 네. 감사합니다.”

이상하게 이 사람 앞에서는 말이 쉽게 나오질 않는다. 드라마에서나 보던 집사라는 이미지 탓일까?

‘아니지. 그렇게 따지면 최 팀장이 더한데.’

잠시 생각하던 나는 김 집사 특유의 분위기 때문일 거라고 결론지었다. 어쩌면 난생처음 타 보는 리무진의 생소함이 한몫했을지도 모르겠다.

‘리무진이라니.’

내부는 넓었고 온갖 물품이 비치되어 있었다. 이를테면 지금 최 팀장이 막 손을 댄 소형 냉장고라든가.

“목 좀 축이시겠습니까?”

“저야 좋죠.”

마침 목이 마르던 차였다.

“물? 술?”

“술도 있어요?”

최 팀장이 고개를 끄덕였다.

“그럼요. 원하시는 거면 뭐든지.”

“아, 그럼 저는 소맥이요. 반반.”

“……물 드릴게요.”

최 팀장이 건네준 생수병엔 그 흔한 상표 하나 없었다.

히말라야 어디서 공수해 왔다는 최 팀장의 말에 나는 내심 혀를 내둘렀다.

‘더럽게 비싸겠네.’

돈지랄도 이런 돈지랄이 없다. 그래도 한 모금 마셔 보니 시원하긴 하다.

꿀꺽.

띠링.



- [히말라야의 정수]를 섭취하셨습니다.

- 한 시간 동안 지력이 1 상승합니다.



……이래서 돈지랄하는구나. 하긴 이래야 부의 재분배가 이루어지고 경제가 활성화되는 거지. 음.

내가 몇 개 챙겨 갈까 고민하고 있을 때 리무진이 멈췄다. 김 집사가 특유의 중후한 목소리로 말했다.

“도착했습니다.”

차에서 내리자마자 보이는 광경에 입이 딱 벌어진다.

높게 솟은 고층 빌딩. 외벽은 마법적인 처리라도 했는지 햇빛을 받지 않아도 반짝거리고, 입구에는 정복을 차려입은 수위들이 대기 중이었다.

“우와. 우와아.”

연신 탄성을 토해 내는 내게 최 팀장이 다가왔다.

“멋지죠? 이곳에 전국 100대 길드의 지부가 전부 모여 있다고 해도 과언이 아닙니다. 태경 씨가 이름만 들으면 아는 해외 거대 길드 지사도 있어요.”

나는 빌딩에서 눈을 떼지 못한 상태로 대답했다.

“땅값이 어마어마하겠네요.”

“그렇죠. 부천 인근 게이트의 중심지라고도 할 수 있으니까.”

“과거의 강남처럼?”

“태경 씨나 저나 그 시절을 살진 않았지만…… 제가 아는 바로는 더했으면 더했지, 덜하진 않을 겁니다.”

땅의 가치가 뒤바뀐 지 오래다.

내가 태어나기도 전의 일이지만, 대격변 이전의 시대를 살았던 중년 헌터들은 가끔 추억에 젖어 그 시절의 이야기를 늘어놓고는 했다.



‘옛날에는 강남에 집 한 채 있으면 금수저 소리 들었지.’

‘우스갯소리로 천당 위에 분당 있다고들 했어, 그만큼 거기가 금싸라기 땅이었다고.’

‘그 정도로 비쌌어요?’

‘토 나올 정도로 비쌌지. 몬스터들이 쳐들어오기 전까지는.’



그 이후는 나도 아는 이야기다. 대격변 초기, 잘 발달된 대도시와 인구 밀집 지역은 몬스터 군단의 첫 표적이었고 인류는 속수무책이었다.

현재의 강남과 분당은 이미 한 번 파괴되었다가 재건된 도시다. 대격변 이후 진짜 금싸라기 땅은 두 종류로 나뉘었다.

‘안전 구역, 그리고 게이트 밀집 지역.’

안전 구역은 게이트 발생 확률이 제로에 가까운, 일반인 최고의 거주지라 할 수 있고 게이트 밀집 지역은 헌터 길드가 자리 잡기에 최적의 요건을 갖춘 곳이다.

‘이를 테면 초등학교 앞 분식집이랄까.’

부천에 존재하는 게이트만 백여 개다. 그중 상당수가 하급 게이트지만 숫자로만 따지면 대한민국을 통틀어 열 손가락 안에 드는 밀집 지역이다.

‘여기가 그 중심지고.’

주위에 가득한 고층 빌딩만 둘러봐도 알 수 있다. 어지간한 중소 길드는 발도 들일 수 없는 동네라는 사실을.

‘이런 재력이라니.’

내가 경외 어린 눈빛으로 최 팀장을 바라보던 그때였다.

“우리도 열심히 해서 저런 곳으로 이사 갑시다.”

“충성을 바치겠…… 예?”

“네?”

“아니, 예?”

“왜 그러십니까?”

시바, 왜 그러긴. 몰라서 물어?

목구멍까지 차오른 말을 간신히 삼킨 후에야 목소리가 새어 나왔다.

“다 도착했다면서요?”

“네, 도착했죠.”

김 집사를 향해 홱 고개를 돌렸다.

“김 집사님. 여기 맞아요?”

“맞습니다.”

망설임 없이 고개를 끄덕인 김 집사가 덧붙였다.

“하지만 헌터님께서 보시는 방향이 잘못된 것 같습니다.”

“방향?”

“네. 그 위치에서 우측으로 좀 고개를 틀어 보시면 될 것 같은데요.”

그의 말대로 고개를 돌린 나는 잠깐의 침묵 끝에 입을 열었다.

“뭡니까, 저 무너져 가는 건물은?”

호화로운 고층 빌딩 사이, 홀로 우두커니 자리한 그 건물은 유난히 작고 낡아 보였다.

김 집사가 친절하게 설명해 주었다.

“정확히는 슈퍼마켓이죠.”

“더 정확히는 구멍가게 같은데요.”

눈을 가늘게 뜨고 무너져 가는 구멍가게를 노려봤다. 때가 누렇게 낀 간판에는 이렇게 적혀 있었다.



[순이네 수퍼]



“순이는 누굽니까? 이름도 촌스럽네.”

“할머니십니다. 여기서 70년 동안 사신.”

“생각해 보니까 참 세련됐네요. 만수무강하실 것 같은 성함.”

“두 달 전에 돌아가셨습니다.”

“아.”

나한테 왜 이러냐.

“엄청난 쇠고집이셔서 밀집 지역 재개발 당시에 어떤 거액을 제시해도 응하지 않으셨죠. 나중에는 다른 길드들도 이미 자리를 잡은 뒤였고…… 결국 유족분들 통해서 저희가 매입했습니다.”

“그럼 저 순이네 수퍼가 우리 길드 하우스라는 말이네요?”

“정확합니다.”

나는 착잡한 눈빛으로 반쯤 무너진 순이네 수퍼를 바라봤다.

길드 하우스는 길드의 얼굴이요, 간판이다. 아무리 동네 땅값이 비싸도 그렇지 저런 곳을…….

‘아니지. 신생 길드가 이 정도면 대단한 거지.’

기대치가 너무 높았던 것뿐이다. 온갖 사기가 판치는 이 바닥에서, 최 팀장이 내게 보여 준 정성만 해도 충분히 믿고 따라갈 만하다.

“최 팀장님.”

“네, 태경 씨.”

나는 최 팀장의 손을 덥석 움켜잡았다.

“저, 진짜 열심히 해 보겠습니다. 길드 하우스가 순이네 수퍼건 순이네 빌딩이건 상관없어요.”

최 팀장이 떨떠름한 얼굴로 대답했다.

“알아주시니 감사합니다.”

“그런 말도 있잖습니까. 시작은 미약하나 그 끝은 창대하리라!”

“지금도 창대한 편인데요. 김 집사님, 저 가게 부지 매입하는데 얼마 들었죠?”

김 집사가 대답했다.

“평당 20억이 약간 넘습니다.”

“……평당 20억이요?”

“예.”

잠깐의 침묵 끝에 내가 입을 열었다.

“시작은 창대하나 그 끝은 더욱 창대할 거라 믿습니다.”

“…….”

“…….”

최 팀장과 김 집사의 시선이 화살처럼 꽂힌다. 두 사람이 뭐 이런 새끼가 있나 하는 표정으로 나를 응시하던 그 순간이었다.

끼이이익. 쿵!



[순이네 수퍼]



한컴 바탕체로 또박또박 적힌 수십 년 역사의 간판이 땅바닥에 처박혔다.

“……리모델링하면 괜찮아질 겁니다.”

최 팀장이 모기 같은 목소리로 중얼거릴 때, 슈퍼 문이 열리고 한 사람이 모습을 드러냈다.

“어이고, 이거 또 떨어졌네.”

투덜거리며 쓰러진 간판을 한 손으로 들어 올리는 괴력의 사내. 전혀 예상치 못한 인물의 등장에 나는 입을 딱 벌렸다.

“꺽정 아저씨?”

사람 좋은 중년의 E급 헌터, 임꺽정이 우리를 발견하고 해맑게 웃으며 손을 흔들었다.

“어, 태경아!”

뭐야, 이거. 어떻게 된 거야?

내가 벙쪄 있는 사이 다가온 임꺽정이 내 어깨를 두드렸다.

“자식. 잘 지냈냐? 너 C급 됐다며?”

“아니, 아저씨가 왜 여기 있어요?”

“으하하! 왜 있기는. 길드원이 길드 하우스에 있는 게 잘못이야?”

호쾌한 웃음을 터트린 그가 말을 이었다.

“병원에 꼼짝 없이 누워 있었는데 갑자기 저기 최 팀장이 찾아와서 그러더라고. 길드 들어올 생각 없냐고. 두말할 것 없이 오케이 했지.”

간판을 슬픈 눈으로 바라보던 최 팀장이 한마디 보탰다.

“믿을 만한 분인 것 같아서요.”

“젊은 사람이 의리가 있어. 저기 김 씨도 과묵해서 그렇지 사람이 참 괜찮더라고. 송 양이야 말할 것도 없고.”

“아니, 잠깐. 잠깐만요.”

이게 지금 무슨 상황이냐.

나는 최대한 침착한 어투로 물었다.

“얼마 전에 가입하셨다고요?”

“응.”

최 팀장이 다시 끼어들었다.

“믿을 만한 분인 것 같아서요.”

“젊은 사람이 의리가 있어. 저기 김 씨도 과묵해서 그렇지…….”

돌겠네.

“그건 아까 들었고요. 그럼 다른 분들은요?”

“응?”

“다른 길드원들은 어디 있어요? 설마 여기 있는 네 명이 전부인 건 아니죠?”

“당연히 아니지.”

딱 잘라 대답한 임꺽정이 덧붙였다.

“송 양은 장 보러 갔어. 너 환영 파티 해 준다고.”

“송 양? 설마 그분이 끝?”

“응. 송 양까지 해서 다섯 명이지. 한 시간도 전에 나갔으니 이제 슬슬 돌아올 때가 됐는데.”

이어지는 말은 귀에 들리지도 않았다.

‘다섯 명이라니.’

이거 꿈인가?

멍한 얼굴로 무너져 가는 순이네 수퍼를 바라보던 나를 깨운 건 임꺽정의 우렁찬 외침이었다.

“어, 저기 오네. 송 양! 여기야, 여기! 신참 왔어!”

나는 임꺽정의 시선을 따라 고개를 돌렸다.

초미니 길드의 마지막 길드원이자 창립 멤버.

‘그녀’가 그곳에 있었다.
```

## Final English reading copy

```markdown
# Chapter 76

Ding.



> **System**
>
> - You have joined the **Peace Guild**!
>
> - You have completed the **Guild Membership** achievement!
>
> - You receive 10 points as an achievement reward.



*This counts as an achievement too?*

Whenever a System message like this appeared, I felt like I had become some kind of hero. An achievement, huh? That was quite an impressive way to package joining a Guild just to make money.

*Well, I’m not complaining.*

Ten points was a pretty sweet reward on its own, but after hearing what Team Leader Choi said next, I had to keep forcing down the corners of my mouth, which kept trying to shoot upward.

“The signing bonus will be processed by the end of today. As for your housing and any other matters…”

A 500 million won signing bonus, a fixed monthly salary of 50 million won, and a seventy-percent settlement share.

A house and a car provided by the Guild, along with dozens of other benefits.

I had already checked everything in the contract several times, but hearing it laid out like this still made it feel new.

*I’ve really made it.*

Until barely three months ago, I couldn’t have imagined my life turning out like this.

The Sleeping Dragon of Shanxi in Murim, and a Hunter in the real world who casually earned hundreds of millions of won a year.

“Team Leader.”

“As for equipment rentals, you can use anything you want apart from my collection… Huh?”

“Could you slap me once? If this is a dream, I’d like to wake up quickly.”

The moment I finished speaking, my vision flashed.

Thwack!

*Wham?* Not *smack*?

I rubbed my stinging jaw and muttered, “You really don’t hold back.”

“I have trouble refusing a request.”

“I don’t think I told you to use your fist.”

“You didn’t tell me not to use it, either.”

“……”

Without the newly acquired **Toughness** stat, I might have gone sprawling in a most undignified fashion.

*Right. This guy was a B-rank Hunter.*

The fist he had thrown without even taking a stance had landed squarely on my jaw. The power and the point of impact had both been perfect.

“Still, don’t people usually use a slap?”

“There are exceptions. So? Are you feeling more awake now?”

“……Very much so.”

“Good. It’s better for making a first impression if you meet them while you’re in your right mind.”

I looked at Team Leader Choi, bewildered by his sudden remark.

“First impression? Who are we meeting?”

“Who do you think?”

Team Leader Choi continued with a smile.

“The other Guild members.”

“Ah.”

Only then did I remember something I had completely forgotten.

A Guild needed at least three people to be established.

“Shall we get going, then?”

Team Leader Choi pointed out the window. A sleek black limousine was gliding into the parking lot in front of the café.



* * *



“Congratulations.”

The owner of that deep, dignified voice, the sort that belonged in a coffee commercial, was Butler Kim. Even in the sweltering summer, he was dressed in a suit and was expertly driving the limousine.

“Oh, yes. Thank you.”

For some reason, I found it difficult to speak naturally in front of this man. Was it because of the image of a butler I had only ever seen in dramas?

*No. If that were the reason, Team Leader Choi would be even worse.*

After thinking about it for a moment, I decided it was because of Butler Kim’s distinctive atmosphere. The unfamiliarity of riding in a limousine for the first time might have had something to do with it, too.

*A limousine.*

The interior was spacious and stocked with all sorts of things. For example, the small refrigerator Team Leader Choi had just opened.

“Would you like something to drink?”

“Sure.”

I happened to be thirsty.

“Water? Alcohol?”

“You have alcohol?”

Team Leader Choi nodded.

“Of course. Anything you want.”

“Then I’ll have soju and beer. Half and half.”

“……I’ll give you water.”

The bottle of water Team Leader Choi handed me didn’t have even the most ordinary brand name on it.

He told me it had been brought in from somewhere in the Himalayas, and I clicked my tongue inwardly.

*That must cost a ridiculous amount.*

What a fucking waste of money. Still, when I took a sip, it was refreshingly cold.

Gulp.

Ding.



> **System**
>
> - You have consumed **Essence of the Himalayas**.
>
> - Your Intelligence increases by 1 for one hour.



……So this was what all that fucking money was for. Well, this was how wealth got redistributed and the economy stayed active. Right.

The limousine came to a stop while I was wondering whether I could sneak a few bottles away.

Butler Kim spoke in his characteristic deep voice.

“We’ve arrived.”

The moment I got out of the car, my jaw dropped at the sight before me.

A skyscraper towered into the sky. Its exterior gleamed even without direct sunlight, as if it had undergone some kind of magical treatment, and guards in formal uniforms stood waiting at the entrance.

“Wow. Woooow.”

As I continued to marvel at the sight, Team Leader Choi approached me.

“Impressive, isn’t it? It wouldn’t be an exaggeration to say that all the branches of Korea’s top one hundred Guilds are gathered here. There are even branches of foreign mega-Guilds whose names you know just from hearing them.”

I answered without taking my eyes off the building.

“Land must be insanely expensive here.”

“It is. You could call this the center of Gate activity around Bucheon.”

“Like Gangnam in the old days?”

“Neither of us lived through that era, but…… from what I understand, this would be more than that, if anything.”

The value of land had been turned upside down long ago.

Though it had happened before I was born, middle-aged Hunters who had lived through the pre-Great Cataclysm era sometimes became nostalgic and went on about what things had been like back then.

“Back then, if you owned even one house in Gangnam, people said you were born with a silver spoon in your mouth.”

“People used to joke that Bundang was above heaven. That’s how valuable the land there was.”

“It was that expensive?”

“Expensive enough to make you puke. At least until the monsters invaded.”



I knew what happened after that. In the early days of the Great Cataclysm, well-developed metropolitan areas and densely populated regions were the first targets of the monster armies, and humanity had been helpless against them.

Present-day Gangnam and Bundang were cities that had already been destroyed once and rebuilt. After the Great Cataclysm, true prime real estate was divided into two types.

*Safe zones and Gate-dense areas.*

Safe zones, where the chance of a Gate appearing was close to zero, were the best places for ordinary people to live. Gate-dense areas, meanwhile, had the ideal conditions for Hunter Guilds to establish themselves.

*Like a snack bar in front of an elementary school.*

There were around a hundred Gates in Bucheon. Many of them were low-level Gates, but by sheer number, it was still one of the ten most densely concentrated regions in all of Korea.

*And this was the center of it.*

I could tell just by looking at the skyscrapers packed around us. This was a neighborhood where your average small or mid-sized Guild couldn’t even set foot.

*What kind of money did this guy have?*

Just as I was looking at Team Leader Choi with awe, he spoke.

“Let’s work hard and move somewhere like that, too.”

“I’ll devote my loyalty to you…… Huh?”

“Pardon?”

“No, what?”

“What’s wrong?”

*Damn it, why do you think? Are you asking because you don’t know?*

I barely swallowed the words that had risen to my throat before managing to speak.

“You said we’d arrived?”

“Yes, we have.”

I abruptly turned toward Butler Kim.

“Butler Kim, is this the place?”

“It is.”

Butler Kim nodded without hesitation, then added, “However, I believe you’re looking in the wrong direction.”

“The wrong direction?”

“Yes. If you turn your head a little to the right from where you’re standing, you should see it.”

I turned my head as he instructed. After a brief silence, I spoke.

“What is that run-down building?”

Amid the luxurious skyscrapers, the building standing there all by itself looked especially small and dilapidated.

Butler Kim kindly explained.

“Strictly speaking, it’s a supermarket.”

“More precisely, it looks like a corner store.”

I narrowed my eyes and glared at the collapsing store. The yellowed sign read:



**Sooni’s Super**



“Who’s Sooni? What a tacky name.”

“She was an old woman who had lived here for seventy years.”

“Now that I think about it, it’s quite elegant. Sounds like a name that promises a long life.”

“She passed away two months ago.”

“Ah.”

*Why is this happening to me?*

“She was incredibly stubborn, so during the redevelopment of the Gate-dense area, she refused no matter how much money they offered. By then, the other Guilds had already established themselves… In the end, we purchased the property from her surviving family.”

“So that Sooni’s Super is our Guild house?”

“Precisely.”

I stared at the half-collapsed Sooni’s Super with mixed feelings.

A Guild house was the face of a Guild. Its signboard. No matter how expensive the land in this neighborhood was, they had really chosen a place like that……

*No, wait. For a newly established Guild, this is incredible.*

It was only that my expectations had been too high. In an industry crawling with scams, Team Leader Choi had shown me enough sincerity that I could trust him and follow his lead.

“Team Leader Choi.”

“Yes, Taekyung?”

I grabbed Team Leader Choi’s hand.

“I’ll really work hard. I don’t care whether our Guild house is Sooni’s Super or Sooni’s Building.”

Team Leader Choi answered with an awkward expression.

“I’m glad you understand.”

“You know what they say. Though the beginning is humble, its end will be magnificent!”

“It’s already magnificent. Butler Kim, how much did it cost to purchase that lot?”

Butler Kim answered.

“A little over two billion won per pyeong.[^1]”

“……Two billion won per pyeong?”

“Yes.”

After a brief silence, I spoke.

“I believe the beginning is magnificent, but the end will be even more magnificent.”

“……”

“……”

The gazes of Team Leader Choi and Butler Kim struck me like arrows. Just as they stared at me with expressions that seemed to ask, *What kind of asshole is this?* a sound rang out.

Screeeech. Crash!



**Sooni’s Super**



The sign, whose decades-old lettering had been neatly written in Hancom Batang, slammed into the ground.

“……It’ll look fine once we remodel.”

Team Leader Choi muttered in a tiny voice. Then the door of the store opened, and someone stepped out.

“Oh dear, it fell again.”

The powerful man grumbled as he lifted the fallen sign with one hand. At the appearance of this completely unexpected person, my mouth fell open.

“Uncle Kkeokjeong?”

The good-natured middle-aged E-rank Hunter, Im Kkeokjeong, spotted us and waved with a bright smile.

“Hey, Taekyung!”

*What the hell? How did this happen?*

While I stood there dumbfounded, Im Kkeokjeong approached and patted me on the shoulder.

“You little punk. Been doing well? I heard you became C-rank.”

“No, why are you here?”

“Hahaha! Why am I here? Is there something wrong with a Guild member being at the Guild house?”

After letting out a hearty laugh, he continued.

“I was stuck lying in the hospital when Team Leader Choi suddenly came to see me and asked if I wanted to join the Guild. I said yes without a second thought.”

Team Leader Choi, who had been looking sadly at the fallen sign, added, “He seemed like someone I could trust.”

“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but he’s a really good man. And Miss Song goes without saying.”

“No, wait. Just a second.”

What was going on here?

I asked as calmly as I could, “You joined recently?”

“Yeah.”

Team Leader Choi cut in again.

“He seemed like someone I could trust.”

“That young man knows what loyalty means. Mr. Kim over there doesn’t say much, but…”

“I heard that part. What about the others?”

“Huh?”

“Where are the other Guild members? Surely these four aren’t all of us?”

“Of course not.”

Im Kkeokjeong answered firmly, then added, “Miss Song went shopping. She said she’d throw you a welcome party.”

“Miss Song? She’s the last one?”

“Yeah. Including Miss Song, there are five of us. She left over an hour ago, so she should be back soon.”

I couldn’t hear anything that came after that.

*There are five of us.*

*Is this a dream?*

Im Kkeokjeong’s booming voice snapped me out of my daze as I stared at the collapsing Sooni’s Super.

“Oh, there she is. Miss Song! Over here, over here! The newbie’s here!”

I followed Im Kkeokjeong’s gaze and turned my head.

The final Guild member of the ultra-tiny Guild, and one of its founding members.

*She* was there.

[^1]: A pyeong is a traditional Korean unit of area equal to approximately 3.3 square meters.
```
