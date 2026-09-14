<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0087.txt",
      "sha256": "badd2b4c3a526f07bc194398711d1e6996bb0039ac54af8508f3cb104d4ae090",
      "bytes": 13055
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "13e8e017c517855f5413bd18e184789d32e1b804716193b9e969bb2ebfabcfda",
      "bytes": 1135
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "be506419130d136e02dfcb32372f22f49997c431f535f44c6f2351a3e2ab8658",
      "bytes": 8369
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2f46678dd6a7365e520c7a9af9c50a4b34f3d5d64d029b335afd4c890acd1a22",
      "bytes": 23901
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ca78fc0938fd089821e4159686c870f484c7faac827f3aeca042d4d1a13ced08",
      "bytes": 7501
    }
  ],
  "estimated_tokens": 12027
}
-->

# Durable State Update — Chapter 87

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 87. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 87. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 87,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 87,
    "continuity_sources": [87],
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
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Changsoo promises to send Taekyung the agreed-upon 4 billion won by tomorrow.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen for his exceptional ice magic.",
    "Im Chunsoo learns that Changsoo transferred 8 billion won to two accounts, fires him, and begins beating him with an ice club.",
    "Sangdong Guild's Team One Leader brings Changsoo to Im Chunsoo's office, which is closed to visitors for half a day."
  ],
  "continuity_sources": [
    86
  ],
  "open_questions": [
    "Whether Im Changsoo actually transfers the promised 4 billion won by tomorrow remains unresolved.",
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved."
  ],
  "safe_through": 86,
  "temporary_decisions": [
    "Use Frozen for 프로즌 and preserve the tiger-father/dog-son wordplay in 호부견자."
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
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |

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
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 대격변     | **Great Cataclysm**   |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 85
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃87화



“엣취!”

후두두둑!

라면과 밥알을 뒤집어쓴 진호 형이 침착하게 물티슈로 얼굴을 문질렀다.

“마음에 안 들면 말로 해, 말로.”

“그런 거 아냐. 갑자기 막 튀어나왔어.”

“변명하지 마. 더 추해 보인다.”

진짠데. 나는 대답 대신 코를 슥 문질렀다.

어떤 놈이 내 욕이라도 하고 있나?

‘생각해 보니까 그럴 만한 놈이 하나 있긴 한데.’

임창수 그 녀석이라면 범행 동기가 충분하다 못해 차고 넘친다. 그래도 뭐, 내게 40억을 선물한 산타클로스니까 욕 몇 번 정도는 기쁘게 먹을 수 있다.

‘혹시나 했는데, 의외로 약속은 지키는 놈이었어.’

나는 아침에 받은 문자를 떠올렸다. 스마트폰에 깔아 둔 은행 어플 알림은 입, 출금 내역을 빠짐없이 알려 준다.



[진태경님의 110-***-*** 계좌에 4,000,000,000원이 입금되었습니다.]



사소한 해프닝이 있었다면 그걸 처음 발견한 게 진호 형이라는 거다. 샤워하겠다고 스마트폰을 방에 놓고 간 게 실수다.

“넌 돈도 많은 놈이 라면이 뭐냐, 라면이?”

“거 되게 말 많네. 소고기 넣어 줬잖아. 소고기라면 싫어?”

“인마, 지금 그 뜻이 아니잖아.”

탕! 진호 형이 거칠게 수저를 내려놨다.

물론 한마디 하려고 그런 게 아니라 배가 불러서다.

“통장에 40억이 있는데 왜 고시원에서 라면을 먹고 있냐 이거지. 내 말은.”

“뭔 상관이야. 내 맘이지.”

“……그렇긴 한데.”

“그리고 돈 들어온 지 한 시간밖에 안 됐거든? 나도 어떻게 해야 될지 모르겠으니까 조용히 해 봐.”

멀쩡한 척하고 있지만 사실은 아까부터 멍하다. 일개미처럼 독하게 돈을 벌어 왔지만 쓰는 곳은 항상 정해져 있었으니까.

그러던 중 거금이 하늘에서 뚝 떨어진 거다.

40억은 많은 일을 할 수 있는 돈이다. 많은 생각이 뒤따를 수밖에 없었다.

“뭔 놈의 고민이 그렇게 많아? 돈 생기면 가장 먼저 하고 싶은 일이 있었을 거 아냐.”

가장 먼저 하고 싶은 일이라…….

‘그거라면 하나 있지.’

후루룩. 마지막 면발을 빨아들인 나는 자리에서 일어났다.

방을 나서기 전 진호 형에게 한마디 남기는 것도 잊지 않았다.

“고마워.”

“별말씀을.”

“냄비 설거지 잊지 말고. 간다.”

“야, 야!”



* * *



“어?”

현관문 앞, 하연이가 눈을 동그랗게 떴다.

“진짜네. 인터폰 화면 보고 설마 했는데.”

“……진짜가 아니면 뭔데.”

“음. 그래픽?”

“그게 오랜만에 만난 오빠한테 할 소리냐?”

“무슨 소리래. 그저께도 와 놓고.”

아, 맞다. 현실 시간으로는 얼마 안 됐지.

워낙 시간 차가 크다 보니 나도 종종 헷갈린다. 신발을 벗으며 물었다.

“뭐 하고 있었어?”

“공부.”

“그러고 보니까 학교는? 평일이잖아.”

하연이가 코맹맹이 목소리로 대답했다.

“열이 39도래. 2교시까지 버티다가 조퇴했어. 어차피 내일부터 여름 방학이라 얼마 전부터는 계속 자습이고.”

“너 이제 방학이냐? 아니, 그 전에 조퇴했는데 공부를 해?

어째 절정 고수보다 얘가 더 대단해 보인다. 난 이상하게 학교에서 엄청 아파도 조퇴하고 집에 오면 아픈 게 싹 낫던데.

열이 39도나 되는 이 상황에서도 공부라니, DNA가 다른가?

“배움에는 끝이 없는 법.”

학생주임 같은 하연이의 말을 뒤로하고 거실로 들어섰다. 집에서는 우리 둘을 제외하곤 인기척 하나 느껴지지 않는다.

“엄마는?”

“은행.”

“기다렸다는 듯이 대답하네.”

“진짠데?”

“엄마가 그러라고 시켰어?”

“응? 뭘?”

누굴 닮았는지 연기가 천연덕스럽다. 만약 그 사실을 모르고 있었다면 깜빡 속아 넘어갔을 것이다.

‘진작 말씀드렸어야 했는데.’

나도 모르게 씁쓸한 웃음이 흘러나왔다. 현관을 향해 되돌아가는 나를 하연이가 붙잡았다.

“어디 가는데?”

“엄마 찾으러.”

“여기 은행이 한두 개야? 밥 차려 줄 테니까 먹고 있어. 잠시 후면 오실 테니까.”

“괜찮아. 은행 가는 거 아니니까.”

“뭐?”

“마트 앞 사거리 식당. 맞지?”

하연이의 손에서 힘이 스르륵 풀렸다.

“……알고 있었어?”

“응. 한참 전부터.”

“엄마가 부탁했어. 비밀로 해 달라고.”

“그것도 알고.”

“오빠, 안 가면 안 돼?”

하연이의 오랜 습관이다. 중요한 부탁에는 꼭 앞에 오빠를 붙이는 것.

“다녀올게.”

나는 하연이의 머리를 헤집어 주고 현관문을 나섰다.

내려가는 엘리베이터 안에서 가만히 손에 남아 있는 녀석의 온기를 생각했다. 이마가 펄펄 끓는 와중에도 녀석이 공부를 하고 있는 이유도.



* * *



주민등록증에 적힌 이름은 하나지만 살면서 불리는 이름은 여러 개다. 올해로 꼭 쉰이 된 김정희도 마찬가지였다.

“아줌마, 여기 삼겹살 2인분 추가요.”

“네, 잠시만요.”

요즘 가장 많이 불리는 이름은 ‘아줌마’다. 그전에는 ‘하연 엄마’. 또 그전에는 ‘태경 엄마’였다. 아이들이 다 크고 일이 바빠지자 들을 수 없게 된 이름들.

그녀의 진짜 이름을 불러 주었던 한 사람은 이미 오래전 세상을 떠났다.



‘정희 씨.’



스물둘에 만난 그는 다정다감했다. 혼란스러웠던 대격변 시기, 대피소에서 만난 두 남녀는 순식간에 사랑에 빠졌다.

행복한 결혼 생활이었다. 세월이 흘러도 그는 여전히 자신의 이름을 불러 주었다.



‘정희야.’



가끔은 다른 사람 앞에서 이름을 불리는 게 부끄러워 물어본 적이 있다.



‘왜 당신은 내 이름만 불러요? 다른 집 남편들은 누구 엄마. 여보. 마누라. 다들 그렇게 부르던데.’

‘그래서 싫어?’

‘아니, 싫은 게 아니라 그냥 궁금해서. 우리 나이도 먹었잖아요.’

‘나이가 뭐가 중요해. 나는 태경 엄마보다 정희를 더 사랑해서 그렇게 부르는 건데.’

‘애들 앞에서 왜 이래요.’

‘어? 엄마 볼 빨개졌다. 엄마 아빠 아침에도 레슬링 해? 맨날 밤에 하던데.’

‘……태경이 오늘부터 일찍 자라.’



이별은 생각보다 일찍 찾아왔다. 예고도 없이 시내 한복판에 열린 게이트로 두 아이는 아버지를 잃었고 그녀는 남편을 잃었다. 유일하게 자신의 이름을 불러 주었던 한 사람을.

“아줌마!”

김정희는 퍼뜩 정신을 차렸다. 파마머리에 화려한 귀걸이를 한 중년 여성이 그녀를 노려보고 있었다.

“아, 네. 사장님.”

“뭐 하느라 사람이 부르는 소리도 못 들어?”

“죄송합니다.”

“불판은? 설거지 끝났어?”

“저어, 그게.”

잠시 다른 생각을 하느라 손이 멈춰 있었다. 싱크대를 확인한 사장이 눈을 치켜떴다.

“아줌마, 일 이따위로 할 거야?”

“…….”

“참 나. 이럴 거면 내가 직접 하지, 뭣 하러 비싼 돈 줘 가면서 아줌마를 고용했겠어? 안 그래?”

김정희는 고개를 푹 숙였고, 주방의 다른 직원들은 사장의 목소리를 못 들은 척 할 일을 계속했다.

‘비싼 돈은 무슨. 가장 바쁜 시간에 최저 시급으로 부려 먹으면서.’

‘나이 먹었으면 철 좀 들지. 화장 떡칠하고 꾸며도 정희 아줌마보다 안 되는 거 뻔히 아니까 괜히 화풀이야.’

‘애초에 지가 카운터를 똑바로 보고 있든가. 놀러 간 사이에 정희 씨가 받은 주문이 몇 갠데.’

하고 싶은 말은 많지만 생각으로 끝내야 한다. 참다못해 김정희를 편들었던 주방 아줌마는 지난주에 잘렸다.

“이래서 내가 맘 편히 자리를 비울 수 있겠어?”

“……죄송합니다.”

“아줌마 아들 헌터라며. 벌이 괜찮을 텐데 집구석에서 음식이나 하지 왜 여기까지 와서 남의 장사에 민폐를…… 아, F급 헌터라 벌이는 별론가?”

사장의 입가에 비웃음이 맺힌 그 순간.

푹 숙이고 있던 김정희의 고개가 천천히 올라갔다.

“사장님. 말씀이 과하시네요.”

“뭐?”

“과하셨다고요.”

“내가 틀린 말이라도 했다는 거야, 지금?”

“네.”

낯선 느낌에 사장은 말문이 막혔다. 늘 조용하고 온순하던 그녀의 눈동자가 깊이 가라앉아 있었다.

“방금 그 말씀, 사과해 주세요.”

“사, 사과?”

“이 자리에서 지금 당장이요.”

“어, 어머. 그래, 내가 한 말 중에 뭐가 틀렸는데? 아줌마 아들 F급 헌터 맞잖아!”

“등급이 그렇게 중요한가요?”

“당연하지. F급 헌터를 어디에다 써? 우리 아들 정도는 돼야 돈도 잘 벌고 여자도 줄을 서는 거지. 이 가게도…….”

“D급 헌터인 아드님께서 차려 주신 거죠. 알아요. 수십 수백 번도 넘게 들었으니까.”

귀를 쫑긋 세우고 있던 직원들이 저도 모르게 고개를 끄덕였다. 사장의 아들 자랑은 하루에도 몇 번씩 듣는 단골 레퍼토리다.

연봉은 얼마고 집은 몇 평이며 차는 뭔지, 효심까지 깊어 어머니 소일거리 삼아 가게도 열어 줬다는 얘기는 너무 자주 해서 이젠 단골손님도 학을 뗀다.

“그럼 잘 알겠네. 나야 취미 삼아 하는 거지만 아줌마는 다르잖아? 아들 벌이가 시원찮으니까 주방 일 하는 거 아니야?”

“네, 아니에요.”

김정희는 차분하게 말을 이어 갔다.

“우리 태경이, 어릴 때부터 부모 속 한 번 안 썩히고 바르게 컸어요. 가족 위해서 지금도 열심히 일하고 있고요. 돈? 부족하지 않게 벌어요.”

“그런 거 다 핑계지.”

“핑계요? 제 자식이 목숨 걸고 벌어 온 돈인데 부모가 되어서 어떻게 그걸 받아 쓸 수 있겠어요?”

“아줌마, 지금 그거 나 들으라고 하는 소리야?”

“그거야 받아들이기 나름이죠. 그리고 기왕 얘기가 나왔으니 말인데. 그 대단한 아드님은 언제쯤 얼굴을 비추나요?”

“뭐, 뭐?”

“제가 여기서 일한 지 1년이 넘어가는데 그 효심 깊은 아들이 한 번도 찾아오질 않아서요. 전화도 안 하는 건 아니죠?”

쥐 죽은 듯 조용해진 주방 안, 얼굴이 시뻘겋게 달아오른 사장이 눈을 부릅떴다.

“자식도 변변찮은 년이 어디서…….”

직원들은 뒤에 나올 말을 알아차렸다. 사장의 따발총 같은 욕과 함께 해고라는 단어가 튀어나올 게 뻔했다.

그러나 그들 중 아무도 김정희의 반응을 예측한 사람은 없었다.

“말조심해. 이 개 같은 년아.”

“……!”

“……!”

순간 폭탄이 떨어진 듯했다. 죽음 같은 침묵과 믿을 수 없다는 듯 흔들리는 눈동자들. 주방의 모두가 자신의 귀를 의심했다.

‘내가 방금 뭘 들은 거지?’

‘정희 아줌마가 욕을? 세상에.’

언제나 순하고 웃음 많던 김정희다. 하루가 멀다 하고 시비를 걸어오는 사장한테도 싫은 소리 한 번 없이 고개를 숙이던 그녀가, 얼음처럼 차가운 눈빛으로 사장을 노려보고 있다.

“뭐, 뭐라고? 너 지금 뭐라고 했어!”

“개 같은 년이라고 했다. 이 썅년아.”

“쌰, 썅년?!”

충격이 가시기도 전에 2차 폭탄이 떨어진다. 외마디 비명처럼 내지른 사장의 외침은 주방 밖 홀까지 울려 퍼졌다.

“방금 누가 욕하지 않았어?”

“너도 들었어? 방금 누가 썅년이라고 했던 것 같은데.”

“뭐야, 직원들끼리 싸우나?”

웅성거림이 커져 갔다. 손님도, 직원도. 가게 안의 모든 사람들의 이목이 주방을 향해 쏠린 그때였다.

저벅저벅.

모자를 눌러쓴 덩치 큰 청년. 언제 들어왔는지, 언제부터 그곳에 있었는지 아무도 알아채지 못했다. 그가 주방을 향해 걸음을 옮기기 전까지는.

“소, 손님. 주문은 제가…….”

황급히 막아서는 남자 직원의 말에 청년이 빙긋 웃었다.

“괜찮아요. 주문 때문에 온 거 아니니까.”

“아니, 그래도 지금은.”

“실례.”

툭.

부드럽게 밀었을 뿐인데 건장한 체구의 직원이 휘청거리며 쓰러진다. 청년은 반쯤 열린 주방문을 거침없이 밀어젖혔다.

그리고…….

“엄마.”

세상에서 가장 사랑하는 사람의 얼굴과 마주했다.
```

## Final English reading copy

```markdown
# Chapter 87

“Achoo!”

Rattle, rattle!

Jinho hyung calmly wiped his face with a wet tissue after getting covered in ramen and grains of rice.

“If you don’t like it, say so. Use words.”

“It’s not like that. It just came out of nowhere.”

“Don’t make excuses. You look even more pathetic.”

But I was telling the truth. Instead of answering, I rubbed my nose.

*Is someone badmouthing me?*

*Now that I think about it, there is someone who might have reason to.*

If it was Im Changsoo, he had more than enough motive. His motive was overflowing. Still, he was the Santa Claus who had given me four billion won, so I was happy to take a few insults.

*I wondered if he would, but the bastard actually kept his promise.*

I remembered the text message I had received that morning. The banking app installed on my smartphone notified me of every deposit and withdrawal without exception.

> Jin Taekyung’s 110-***-*** account has been credited with 4,000,000,000 won.

The only minor incident was that Jinho hyung had been the first to discover it. Leaving my smartphone in my room when I went to take a shower had been a mistake.

“You’ve got plenty of money, so why are you eating ramen?”

“You sure are talkative. I put beef in it. You don’t like beef ramen?”

“That’s not what I mean, you punk.”

Bang!

Jinho hyung roughly set down his utensils.

Of course, he hadn’t done it to make a point. He was just full.

“I mean, you’ve got four billion won in your bank account, so why are you eating ramen in a goshiwon?[^1]”

“What’s it to you? I’ll do what I want.”

“…That’s true.”

“And the money only came in an hour ago, all right? I don’t know what to do with it either, so be quiet and let me think.”

I was pretending to be fine, but I had been dazed for a while. I had worked myself to the bone like a worker ant, but the money had always been earmarked for something.

Then a fortune had dropped out of the sky.

Four billion won was enough money to do a lot of things. Naturally, a lot of thoughts followed.

“What are you thinking so hard about? There must have been something you wanted to do first as soon as you got money.”

The thing I wanted to do first…

*There is one thing.*

Slurp.

After sucking in the last strand of noodles, I stood up.

Before leaving the room, I didn’t forget to leave Jinho hyung one parting remark.

“Thanks.”

“Don’t mention it.”

“Don’t forget to wash the pot. I’m off.”

“Hey, hey!”

* * *

“Huh?”

Hayeon’s eyes went round when she saw me standing in front of the front door.

“So it really is you. I saw you on the intercom screen and thought, no way.”

“…If it wasn’t really me, what would I be?”

“Hmm. A graphic?”

“Is that any way to talk to your older brother after not seeing him for so long?”

“What are you talking about? You came the day before yesterday.”

Ah, right. Not much time had passed in the real world.

The time difference was so large that I sometimes got confused myself. As I took off my shoes, I asked,

“What were you doing?”

“Studying.”

“Come to think of it, what about school? It’s a weekday.”

Hayeon answered in a nasal voice.

“They said my fever was thirty-nine degrees. I stuck it out until second period, then left early. Summer vacation starts tomorrow anyway, and we’ve been doing nothing but self-study lately.”

“You’re already on vacation? No, wait. You left school early because you were sick, and you’re studying?”

Somehow, she seemed more impressive than a Peak master. Whenever I got really sick at school, my illness mysteriously disappeared as soon as I left early and came home.

She had a raging fever, and she was still studying. Was her DNA different from mine?

“There is no end to learning.”

Leaving Hayeon, who sounded like a school disciplinarian, behind, I entered the living room. Apart from the two of us, there wasn’t a sign of anyone else in the house.

“Where’s Mom?”

“The bank.”

“You answered that awfully quickly.”

“It’s true.”

“Did Mom tell you to say that?”

“Huh? Tell me to say what?”

I wondered who she took after. Her acting was so natural that if I hadn’t known the truth, I would have been completely fooled.

*I should have told her long ago.*

A bitter smile escaped me before I could stop it. As I turned back toward the entrance, Hayeon grabbed me.

“Where are you going?”

“To find Mom.”

“There’s more than one bank around here. I’ll make you something to eat, so wait here. She’ll be back soon.”

“It’s fine. I’m not going to the bank.”

“What?”

“The restaurant at the intersection in front of the supermarket. Right?”

The strength slowly drained from Hayeon’s hand.

“…You knew?”

“Yeah. For a long time.”

“Mom asked me to keep it a secret.”

“I know that too.”

“Oppa, can’t you stay?”

It was one of Hayeon’s longtime habits. Whenever she had an important favor to ask, she always put *oppa* first.

“I’ll be back.”

I ruffled Hayeon’s hair and left the house.

As the elevator carried me down, I quietly thought about her warmth still lingering in my hand—and why she was studying even while her forehead was burning up.

* * *

A person had only one name written on their resident registration card, but they could be called by many names over the course of their life. Kim Jeonghee, who had turned exactly fifty that year, was no different.

“Ajumma, two more servings of pork belly over here.”

“Yes, just a moment.”

The name she was called most often these days was *ajumma*.[^2] Before that, it had been “Hayeon’s mom.” Before that, “Taekyung’s mom.” Once the children had grown up and work had become busy, those names had disappeared from her life.

The one person who had called her by her real name had already passed away long ago.

*Jeonghee.*

She had met him when she was twenty-two. He had been kind and affectionate. During the chaotic period of the Great Cataclysm, the two of them met in a shelter and fell in love at once.

It had been a happy marriage. Even as the years passed, he continued to call her by name.

*Jeonghee.*

Sometimes, embarrassed to hear him call her by name in front of other people, she had asked him about it.

*Why do you only call me Jeonghee? Other husbands call their wives “so-and-so’s mom,” “honey,” or “the missus.” That’s what everyone else does.*

*Does it bother you?*

*No, it’s not that. I was just curious. We’re getting older too.*

*What does age have to do with it? I call you Jeonghee because I love you as Jeonghee more than I love you as Taekyung’s mom.*

*Why are you acting like this in front of the kids?*

*Uh-oh, Mom’s cheeks are red. Mom and Dad, do you wrestle in the mornings too? You do it every night.*

*…Taekyung, starting today, go to bed early.*

Their parting came earlier than expected. Without warning, a Gate opened in the middle of downtown. The two children lost their father, and she lost her husband—the one person who had been the only one to call her by name.

“Ajumma!”

Kim Jeonghee jolted back to reality. A middle-aged woman with permed hair and flashy earrings was glaring at her.

“Oh, yes, ma’am.”

“What were you doing that you couldn’t even hear me calling you?”

“I’m sorry.”

“What about the grill plates? Are you done washing them?”

“Well, the thing is…”

Her hands had stopped while she was lost in thought. The owner checked the sink and raised her eyes sharply.

“Ajumma, are you going to work like this?”

“…”

“Honestly. If this is how you’re going to do things, I should do it myself. Why would I pay good money to hire you? Am I wrong?”

Kim Jeonghee lowered her head, while the other kitchen workers continued what they were doing, pretending not to hear the owner’s voice.

*Good money, my ass. She works us at minimum wage during the busiest hours.*

*She’s old enough to know better. She knows perfectly well that no amount of caked-on makeup and dressing up will make her a match for Jeonghee ajumma, so she’s taking it out on her.*

*She should watch the counter properly herself in the first place. How many orders did Jeonghee receive while she was off having fun?*

There were many things they wanted to say, but they could only keep them to themselves. The kitchen ajumma who had finally lost her patience and stood up for Kim Jeonghee had been fired last week.

“Can I really leave this place with you in charge?”

“…I’m sorry.”

“I heard your son is a Hunter. He should be making decent money, so why don’t you just stay home and cook? Why come all the way here and be a nuisance to someone else’s business? Ah, is his income not very good because he’s an F-rank Hunter?”

The moment a sneer appeared at the corners of the owner’s mouth, Kim Jeonghee slowly raised her bowed head.

“Boss. That was too much.”

“What?”

“I said you went too far.”

“Are you saying I was wrong?”

“Yes.”

The unfamiliar sensation left the owner speechless. Kim Jeonghee had always been quiet and gentle, but now her eyes had sunk into a deep, cold stare.

“Please apologize for what you just said.”

“A-apologize?”

“Right here. Right now.”

“O-oh my. Fine. Which part of what I said was wrong? Your son really is an F-rank Hunter!”

“Is his rank really that important?”

“Of course it is. What good is an F-rank Hunter? A son like mine has to make good money and have women lining up for him. This shop, too…”

“Your son, the D-rank Hunter, set it up for you. I know. I’ve heard it dozens, if not hundreds, of times.”

The employees, who had pricked up their ears, unconsciously nodded.

The owner’s boasting about her son was a familiar routine they heard several times a day.

How much he made, how big his house was, what kind of car he drove, and how filial he was—so filial that he had even opened a shop for his mother to have something to do. She had repeated it so often that even the regular customers were sick of hearing it.

“Then you know all about it. I run this place as a hobby, but you’re different, aren’t you? You’re working in the kitchen because your son doesn’t make enough money, aren’t you?”

“No, that’s not it.”

Kim Jeonghee continued calmly.

“Our Taekyung grew up right. He never once caused his parents any trouble, even when he was little. He’s still working hard for his family. Money? He earns more than enough.”

“That’s all an excuse.”

“An excuse? This is money my child earned by risking his life. How could I, as his parent, accept it and spend it?”

“Ajumma, are you saying that for my benefit?”

“That depends on how you choose to take it. And since we’re on the subject, when does that amazing son of yours ever show his face?”

“What?”

“I’ve worked here for over a year, but that devoted son of yours hasn’t visited even once. He does at least call you, doesn’t he?”

The kitchen fell silent as death. The owner’s face turned bright red, and her eyes widened.

“Where does a bitch with such a pathetic son get off—”

The employees knew what was coming next. Along with the owner’s machine-gun burst of abuse, the word “fired” was bound to come flying out.

But none of them could have predicted Kim Jeonghee’s reaction.

“Watch your mouth, you goddamn bitch.”

“…”

“…”

It was as if a bomb had gone off.

A deathly silence descended, and everyone’s eyes shook with disbelief. Every person in the kitchen wondered if they had heard correctly.

*What did I just hear?*

*Did Jeonghee ajumma just swear? My God.*

Kim Jeonghee had always been gentle and quick to smile. Even though the owner picked fights with her day after day, she had always bowed her head without a single word of complaint. Now she was glaring at the owner with eyes as cold as ice.

“W-what did you say? What did you just call me?”

“I called you a goddamn bitch, you fucking bitch.”

“Y-you fucking bitch?!”

Before the shock had even faded, a second bomb went off. The owner’s shriek rang all the way out into the dining area.

“Did someone just swear?”

“You heard that too? I think someone just called somebody a fucking bitch.”

“What the hell? Are the employees fighting?”

The murmuring grew louder. Customers and employees alike turned their attention toward the kitchen.

That was when it happened.

Thud. Thud. Thud.

A large young man with his cap pulled low. No one had noticed when he entered, or how long he had been standing there. Not until he started walking toward the kitchen.

“S-sir. I’ll take your order…”

The young man smiled faintly at the male employee who hurried to stop him.

“It’s okay. I didn’t come to order.”

“No, but still, right now…”

“Excuse me.”

Tap.

He had only given the employee a gentle push, but the burly man staggered and fell. The young man pushed open the half-open kitchen door without hesitation.

And then…

“Mom.”

He came face-to-face with the person he loved most in the world.

[^1]: A goshiwon is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.
```
