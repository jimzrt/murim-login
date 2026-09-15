<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0101.txt",
      "sha256": "71480faaa1e1c3074a50be58c2c0e3ddc33894c4ab1ab39e5c709f17b92f070f",
      "bytes": 13225
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4a8f7a88831eaa14e58993f58ef8750408e55db037c3be4ebb860fedf84aee41",
      "bytes": 2018
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "43155cc661a53ae1d57b2a0b798ab13bf82f30de31725512f2a5b24d91b69590",
      "bytes": 12286
    },
    {
      "path": "characters/Im Chunsoo.md",
      "sha256": "04576a2f61bde8da6a3711de4405caf2a82445afee973e680ea6b0c260a001e0",
      "bytes": 715
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "10ffaf5617559928d08c9f4875fcd2aba2ffd4e925558c5498a9cf0c866487e0",
      "bytes": 23943
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "ce14a47bb219f2b28b61c0e67775498dc599a93d4f57931feb8cae2d45050c8c",
      "bytes": 487
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3b48e246a15b7ad98c10d604647f2713362f5e4d669ccf12a929581dc5db68de",
      "bytes": 11888
    }
  ],
  "estimated_tokens": 14735
}
-->

# Durable State Update — Chapter 101

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 101. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 101. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 101,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 101,
    "continuity_sources": [101],
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
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung under Im Chunsoo's direction.",
    "Choi Byungil led the failed operation against Taekyung and was defeated alongside the other five field Hunters.",
    "Kim Junsu is the Security Team's sole Familiar mage and revealed the operation's information when Taekyung threatened his remaining hair.",
    "Hong Woojin was a B-rank Familiar mage hired from outside by Team Leader 1.",
    "Taekyung seized the Security Team's supplies, treated the wounded Hunters, and held them until Team Leader 1 released them.",
    "Im Chunsoo initiated the investigation after Im Changsoo was extorted for a hundred million won.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Im Chunsoo attacked Taekyung with roughly a dozen ice spikes after inviting him to walk.",
    "Taekyung evaded the ice spikes by casting Fire Wall.",
    "Kim Hwajong is a Level 80 mage and Butler Kim who arrives at the hiking-trail confrontation.",
    "The property being used as the surveillance base remains unidentified.",
    "The reason Kim Hwajong arrived at the confrontation is unknown."
  ],
  "continuity_sources": [
    99,
    100
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation and what role he intends to play remain unknown."
  ],
  "safe_through": 100,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술.",
    "Keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you while preserving his blunt senior voice.",
    "Render 김화종's 춘수 as Chunsoo."
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
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |

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
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 임춘수    | **Im Chunsoo**    |
| 살기     | **killing intent**                               |                                                       |
| 창기     | **Spear Energy**                                 | Explicit system skill for Taekyung                    |
| 선배     | **Senior**                                   |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 평화 | **Peace Guild** | Guild name. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

## Listed compact profiles

### Im Chunsoo.md

# Im Chunsoo (임춘수)

- **Safe through:** Chapter 100
- **Aliases:** Frozen
- **Role:** Level 75 A-rank Hunter; founder and Guild Master of Sangdong Guild; renowned ice mage who personally confronted Jin Taekyung
- **Personality:** Intimidating, severe, and extremely short-tempered, though he has tried to moderate his temper with age
- **Voice:** Sharp and commanding, with a comparatively gentle tone when deliberately controlling his temper; becomes violently profane when enraged
- **Relationships:** Father of Im Changsoo, whom he considers a pathetic disappointment and immediately fires and punishes after learning of Changsoo's actions

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 100
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 100
- **Aliases:** Butler Kim
- **Role:** Level 80 mage known as Butler Kim; arrives at the confrontation between Im Chunsoo and Jin Taekyung
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Addresses Im Chunsoo familiarly as Chunsoo; appears at the hiking-trail entrance during Chunsoo's confrontation with Jin Taekyung

## Korean source

```text
＃101화



‘뭐야, 이거.’

어안이 벙벙했다. 김 집사의 등장도 뜻밖이지만 그가 임춘수를 향해 건넨 말에 비하면 아무것도 아니다.

‘춘수? 자네?’

두 사람 아는 사이였어?

생각해 보면 김 집사와 임춘수는 공통점이 많았다. 나이도 엇비슷하고 헌터 경력도 오래됐다.

‘그러고 보니 김 집사도 대격변 때 헌터로 활동했지.’

당사자의 입으로 직접 들은 건 아니지만 내심 짐작하고 있었던 사실이다. 두 사람을 번갈아 쳐다보던 나는 조심스럽게 물었다.

“두 분, 친하세요?”

임춘수의 눈동자가 파르르 떨렸다.



* * *



처음 평화 길드에 관한 보고서를 받았을 때, 임춘수는 자신의 눈을 의심했다.

흐릿한 기억 속에 남아 있는 얼굴, 다시는 볼 수 없을 거라 확신했던 얼굴이 보고서 속 사진에 있었기 때문이었다.



‘이, 이 자가 누구라고?’

‘평화 길드 마스터 김화종. 나이는 55세. B급 헌터입니다.’

‘김화종? B급 헌터?’

‘예. 혹시 무슨 문제라도?’

‘아, 아니야. 전에 알던 사람이랑 닮아서 착각했어.’



그럼 그렇지. 임춘수는 안도의 한숨을 내쉬었다.

얼굴이 약간 닮긴 했지만 그것뿐이다. 무엇보다 그자는 이미 30여 년 전 죽지 않았나.

아무리 세상이 요지경이 됐다지만 죽은 자가 살아 돌아올 수는 없다.

‘설령 그 인간이 살아 돌아왔어도 이런 곳에서 썩고 있진 않겠지. 늙다리 B급 헌터랑 착각한 것뿐이야.’

그날, 임춘수는 오랜만에 소주를 한 잔 걸치며 찜찜한 마음을 털어 냈다. 50이 넘도록 그의 발목을 붙잡고 있는 끔찍한 기억들을 떨치려는 시도였다.

‘어후, 이 나이 먹고도 아직 이러고 있다니.’

이후 김화종의 정보에 철통같은 보안이 걸려 있다는 얘길 들었을 때는 등줄기가 서늘하기까지 했었다.

‘설마? 아냐. 그럴 리가 없지.’

하지만…… 왜 불길한 예감은 틀리는 법이 없을까?

“솟구쳐라. 파이어 월.”

주문을 영창하는 나직한 목소리가 들림과 동시에 솟아오른 불의 장벽.

화륵, 화아악!

초고온의 청염(靑炎)이 강철보다 단단한 얼음송곳을 흔적도 없이 증발시켰다.

그리고…….

“늦지 않아서 다행입니다. 춘수, 자네도.”

꿈에서도 잊을 수 없던 목소리를 듣는 순간, 임춘수는 떠올렸다. 놈에게 지배당했던 공포를. 살기 위해 굴렀던 굴욕을.

‘시발…… 좆 됐다.’

돌처럼 굳은 그에게 진태경이 묻는다.

“두 분, 친하세요?”

뭐? 친하냐고?

임춘수는 폐부 깊숙한 곳에서 올라오려는 쌍욕을 꿀꺽 삼키고 돌아섰다. 오래전 죽었다고 생각했던 한 사람이 그곳에 있었다.

“교, 교관님.”

김 집사가 부드럽게 웃었다. 시간이 흐른 지금까지도 임춘수의 뇌리 깊숙이 새겨진 악마의 웃음.

“28연대 1대대 2중대. 임춘수. 그래, 처음 보자마자 알았지.”

그것은 영혼의 울림이었다.

임춘수의 구부정했던 허리가 펴지고 바짝 붙인 발은 45도. 시선은 전방 15도 위를 향한다.

번개처럼 빠른 동작 끝에 천둥 같은 외침이 터져 나왔다.

“1번 훈련생! 이임! 추운! 수우!”

30년 만에 외치는 관등성명에 산이 들썩였다.



* * *



산 위로 올라간 1팀장이 발견한 것은 핏물이 군데군데 튄 풀숲과 마법 밧줄로 꽁꽁 묶인 보안팀이었다.

‘정말 가관이군, 가관이야.’

내심 혀를 찬 그가 검을 꺼내 밧줄을 끊었다.

다들 피는 좀 흘렸어도 심각한 부상을 입은 것 같아 보이지는 않는다. 진태경이라는 놈이 최소한의 신경은 써 준 모양이었다.

‘이 정도면 B급 최상위. 혹은 A급 헌터.’

1팀장의 판단으로 진태경의 실력은 그 정도 되는 듯했다.

그 후 산에서 내려오는 길은 누군가에게는 지옥 같은 시간이었다.

“왜 그랬습니까? 감시 정도야 어떻게 넘기겠지만 오늘 일은 살인미수까지 갈 수도 있어요. 뒷일은 생각하고 일을 벌인 겁니까?”

“……죄송합니다.”

1팀장의 말에 보안팀장이 고개를 푹 숙였다.

무리수까지 둬 가며 무력행사에 나섰는데 도리어 진태경에게 탈탈 털렸다. 입이 열 개라도 할 말이 없는 상황이다.

“길드장님께서 단단히 실망하셨습니다.”

“그, 그럼?”

“시말서에 감봉은 당연한 거고 그 이상까지 각오해 두세요.”

“사직, 입니까?”

“그거야 길드장님 뜻에 달린 거죠.”

“……저, 팀장님. 혹시.”

“미리 말해 두는데, 괜한 청탁 같은 건 하지 않길 바랍니다. 내가 다니는 직장 이름에 똥칠한 사람을 편드는 취미는 없어서요. 길드장님 뜻에 반대할 생각도 없고.”

“…….”

“후우.”

1팀장이 짜증 섞인 한숨을 내쉰 그때였다.

저 멀리서 울려 퍼지는 쩌렁쩌렁한 외침.

- 1번 훈련생! 이임! 추운! 수우!

“……?”

“……?”

뭐지? 환청인가?

1팀장은 물론이고 죽을상을 하고 있던 보안팀원들까지 화들짝 놀랐다. 가장 먼저 정신을 수습한 건 보안팀장이었다.

“저기, 1팀장님. 이런 분위기에서 죄송합니다만, 방금 길드장님 목소리를 들은 것 같은데요.”

귀를 후비고 있던 1팀장이 눈을 동그랗게 떴다.

“……보안팀장도 들었어요?”

“저희도 들었는데요.”

“근데 길드장님 목소리인지는 잘 구분을 못 하겠고…… 성함은 들은 것 같습니다.”

“그게 사람 이름이었어? 난 그냥 악쓰는 소리 같던데.”

“그런가? 나는 관등성명 대는 것처럼 들렸는데.”

보안팀의 쑥덕거림을 듣던 1팀장이 정색했다.

“방금 말한 사람 누굽니까? 뭐, 관등성명?”

그에게 있어 임춘수는 존경하는 선배이자 상관이었다.

대격변 때부터 활동한 불세출의 헌터이자 전쟁 영웅이 난데없이 관등성명이라니?

상상한 적도 없고 상상할 수도 없다.

“아직도 그런 헛소리를 할 여유가 있습니까? 이게 도대체 정신이 똑바로 박힌 사람들이 할 얘기냔 말이야!”

“죄, 죄송합니다.”

“저희가 잘못 들은 것 같습니다.”

“다들 정신 똑바로 차려요. 알겠습니까?”

으름장을 놓은 1팀장이 다시 걸음을 뗀 그 순간이었다.

- 아닙니다아아악!

“…….”

- 시정하겠습니다아악!

“…….”

그것은 영혼이 실린 이등병의 외침.

꾹 닫혀 있던 1팀장의 입이 열린 것은 잠시 후였다.

“지금부터 전속력으로 뛰어간다. 실시.”

“시, 실시!”

이 자리에 모인 이들은 최소 C급 헌터. 이미 일반인의 한계를 훌쩍 뛰어넘은 초인들이다.

폭주 기관차처럼 내달린 그들은 5분이 채 지나기도 전에 등산로 입구에 도착했다.

“느려 터졌군. 이제야 왔나?”

“길드장님!”

“목소리 줄여, 귀청 떨어져.”

여느 때와 다름없는 임춘수의 모습에 1팀장이 안도의 한숨을 내쉬었다.

“전 또 혹시 무슨 일이 난 줄 알고…….”

“일이라니? 뭐 이상한 일 있었나?”

“아, 아닙니다. 그런데 진태경 그놈은 어디 갔습니까?”

“적당히 타일러서 보냈어. 이야기를 나눠 보니 생각보다 괜찮은 놈이더군. 그런데 왜?”

“놈이 무슨 소란을 피웠나 해서요.”

“아, 혹시 아까 어떤 놈이 소리 지른 거 말하는 거야?”

“네, 맞습니다. 그런데 목소리가 꼭…….”

길드장님 같아서요. 차마 뒷말을 잇지 못하는 1팀장을 향해 임춘수가 눈을 부라렸다.

“목소리가 뭐?”

“아, 아무것도 아닙니다.”

“싱겁기는. 새파란 놈들이 저 아래서 군대놀이 하길래 쫓아내고 왔다. 아니, 요즘도 대학에 군기 문화가 있어?”

“아, 그렇군요.”

“거 뭐야. PT 체조로 잠깐 굴렸더니 아주 죽으려고 하데?”

1팀장은 마음에 품고 있던 의혹이 말끔하게 사라지는 것을 느꼈다.

‘내가 미쳤던 거지. 감히 무슨 생각을.’

그가 한쪽에서 마음 깊이 반성하고 있을 때 임춘수는 보안팀을 탈탈 털고 있었다.

“보안팀장.”

“예, 옛!”

“어쭈. 대답은 잘하네. 이런 일을 벌이고도 아직 팀장은 팀장이라 이건가?”

“죄, 죄송합니다!”

“다른 놈들은 잘해서 입 다물고 있나? 오늘 칼춤 한번 춰?”

“죄송합니다, 길드장님!”

1팀장은 흐뭇하게 웃으며 그 광경을 지켜봤다.

간혹 임춘수의 성격이 지랄 맞다는 유언비어를 퍼트리는 놈들이 있다. 그러나 직접 옆에서 지켜본 그는 카리스마가 뛰어난 상관이며 훌륭한 인생의 선배였다.

‘길드장님. 영원히 따르겠습니다.’

무한한 존경의 눈빛으로 임춘수의 뒷모습을 바라보던 1팀장이 문득 고개를 갸웃했다.

‘……그런데 왜 길드장님 등에 흙이 묻어 있지?’

애들을 좀, 격하게 혼내셨나 보다.



* * *



“도착했습니다.”

김 집사의 말에 조수석에 앉아 있던 나는 화들짝 정신을 차리며 주변을 두리번거렸다. 창밖으로 아파트 입구가 보였다. 언제 여기까지 왔지?

“가, 감사합니다.”

“별말씀을요.”

멋있게 주름진 얼굴에 미소가 떠오른다. 왕년에 한 시대를 주름잡던 중년 배우가 생각나는 모습이다.

‘아니, 이 사람도 한 시대를 주름잡긴 했구나.’

지금까지는 그저 까마득한 선배 헌터 정도로 생각했는데, 그건 김 집사를 몰라도 한참 몰랐던 거다.

‘A급 마법사를, 그것도 임춘수를 개처럼 굴리다니.’

옛 전쟁 영웅한테 PT 8번 100세트를 시키더니, 나중에는 구둣발로 쪼인트를 깠다. 나긋나긋한 목소리로 임춘수를 갈구던 모습은 지금 생각해도 소름 그 자체다.



‘훈련생, 누가 PT 체조에 마나를 씁니까?’

빡!

‘1번 훈련생 임춘수. 죄, 죄송합니다.’

‘아픕니까? 나이 먹더니 목소리도 작아진 겁니까?’

‘아닙니다아아악!’

‘차렷. 열중쉬어. 차렷. 열중쉬어.’

파바바바박!

‘뒤로 취침. 앞으로 취침. 뒤로 취침. 뒤로 취침.’

‘헉.’

‘훈련생, 본 교관이 뒤로 취침이라고 하는 말 못 들었습니까? 정신 똑바로 차립니다.’

‘시정하겠습니다아악!’

‘그리고 왜 선량한 후배를 괴롭힙니까? 본 교관이 누누이 강조하지 않았습니까. 선후배끼리 서로 도우며 살라고.’

‘죄, 죄송합니다.’

‘복명복창합니다. 앉으면서 후배를, 일어나면서 아끼자. 하나. 둘.’

‘후배를, 아끼자!’

‘훈련생, 25기로 기억하는데 맞습니까?’

‘1번 훈련생 임춘수. 예, 그렇습니다.’

‘본 교관은 3기입니다. 만약 오늘 있었던 일이 밖으로 새어 나가거나 다시 반복된다면 4기부터 24기까지 열외 없이 집합입니다.’

‘…….’

‘왜 대답이 없습니까. 쪼그려 뛰기 준비.’

‘주, 준비…….’



굴리고, 굴리고, 또 굴리고.

그야말로 돈 주고도 못 보는 광경. 만약 상동 길드원들이 봤다면 오늘 부로 길드 문 닫을 뻔했다.

‘김 집사, 이 양반 도대체 정체가 뭐야?’

헌터 훈련소 3기면 전국 길드장들을 연병장에 모아 놓고 줄 빠따를 쳐도 된다. 게다가 무려 교관 출신이라니.

어지간한 대격변 초창기 마법사들은 전부 그의 손을 거쳤다고 해도 과언이 아니다.

‘마법사로서의 역량도 최소 A급.’

임춘수가 찍소리도 못하고 얼차려를 당하는 것만 봐도 알 수 있다. 김 집사가 짬으로도, 실력으로도 앞선다.

얼음과 화염. 마법의 상성도 있겠지만 임춘수를 가르쳐서 지금의 위치까지 오르게 한 것도 김 집사라고 볼 수 있다.

‘그런데…….’

그 정도씩이나 되는 사람이 왜 집사 노릇을 하고 있냐 이거지. 슬쩍 김 집사를 곁눈질하다가 시선이 딱 부딪쳤다.

“묻고 싶은 게 많아 보이는군요.”

“솔직히 말씀드리면 그렇습니다.”

궁금해서 도저히 못 참겠다.

생각이 고스란히 드러나는 내 표정에 김 집사가 입꼬리를 말아 올렸다.

“말하자면 깁니다.”

“괜찮습니다. 휴가 중이라 시간 넉넉해요.”

“아, 그럼 이참에 진태경 씨 얘기도 들을 수 있겠군요. 안 그래도 궁금한 점이 한두 가지가 아닌데.”

“생각해 보니까 벌써 저녁 시간이네요. 내일은 휴가 마지막 날이라 부동산 계약도 해야 하고. 허허허.”

“…….”
```

## Final English reading copy

```markdown
# Chapter 101

*What the hell is this?*

I was dumbfounded. Butler Kim’s appearance was unexpected, but that was nothing compared to the words he had directed at Im Chunsoo.

*Chunsoo? You?*

*Were the two of them acquainted?*

Come to think of it, Butler Kim and Im Chunsoo had a lot in common. They were around the same age, and both had been Hunters for a long time.

*Come to think of it, Butler Kim was active as a Hunter during the Great Cataclysm, too.*

I had never heard it directly from him, but I had suspected as much. Looking back and forth between the two men, I carefully asked,

“Are you two close?”

Im Chunsoo’s pupils trembled.

* * *

When Im Chunsoo first received the report on the Peace Guild, he had doubted his own eyes.

The face in the photograph was one that remained in his hazy memories—a face he had been certain he would never see again.

*Who did you say this man was?*

*Peace Guild Master Kim Hwajong. He’s fifty-five years old and a B-rank Hunter.*

*Kim Hwajong? A B-rank Hunter?*

*Yes. Is there some problem?*

*No, no. He resembles someone I used to know, so I mistook him for that person.*

That figures. Im Chunsoo let out a sigh of relief.

The face did resemble him a little, but that was all. More importantly, hadn’t that man died over thirty years ago?

No matter how bizarre the world had become, the dead could not come back to life.

*Even if that bastard had come back to life, he wouldn’t be rotting away in a place like this. I simply mistook him for an old B-rank Hunter.*

That day, Im Chunsoo drank a glass of soju for the first time in a long while and tried to shake off his uneasy feelings. It was an attempt to cast off the terrible memories that had clung to his ankles even after he turned fifty.

*Damn. I’m this old, and I’m still like this.*

Later, when he heard that Kim Hwajong’s information was protected by airtight security, he had even felt a chill run down his spine.

*Could it be? No. There’s no way.*

But then… why did ominous premonitions never turn out to be wrong?

“Rise up. Fire Wall.”

A quiet voice chanting a spell rang out, and a wall of fire surged upward.

*Fwoosh! Fwoosh!*

Blue flames burning at an extreme temperature vaporized the ice spikes, which were harder than steel, without leaving a trace.

And then—

“I’m glad I’m not too late. You too, Chunsoo.”

The moment he heard the voice he could never forget, not even in his dreams, Im Chunsoo remembered.

The terror of being controlled by that man.

The humiliation of rolling around on the ground to survive.

*Fuck… I’m screwed.*

As he stood frozen like a stone, Jin Taekyung asked him,

“Are you two close?”

What? Close?

Im Chunsoo swallowed the stream of curses rising from the depths of his lungs and turned around.

A man he had believed had died long ago was standing there.

“I-Instructor.”

Butler Kim smiled gently. It was the smile of a demon still deeply engraved in Im Chunsoo’s mind, even after all these years.

“Twenty-eighth Regiment, First Battalion, Second Company. Im Chunsoo. Yes, I knew the moment I saw you.”

It was the resonance of the soul.

Im Chunsoo’s hunched back straightened. His feet snapped together at a forty-five-degree angle, and his gaze turned fifteen degrees upward toward the front.

After a series of movements as fast as lightning, a thunderous shout burst from his throat.

“Trainee Number One! Im! Chun! Soo!”

The mountain shook as he bellowed out his military identification for the first time in thirty years.

* * *

What Team Leader 1 found after climbing up the mountain was grass splattered with blood in several places and the Security Team bound tightly with magical ropes.

*What a sight.*

Clicking his tongue inwardly, he drew his sword and cut through the ropes.

Everyone had lost some blood, but none of them appeared to have suffered serious injuries. Jin Taekyung seemed to have shown them at least the bare minimum of consideration.

*At this level, he’s either a top-tier B-rank… or an A-rank Hunter.*

That was how strong Jin Taekyung appeared to Team Leader 1.

For one person, the walk back down the mountain was a hellish experience.

“Why did you do that? We might have been able to overlook the surveillance, but what happened today could amount to attempted murder. Did you start this after thinking about what would happen afterward?”

“I’m… sorry.”

At Team Leader 1’s words, the Security Team Leader hung his head.

They had gone so far as to use force, only to be thoroughly trounced by Jin Taekyung. Even if he had ten mouths, he would have had nothing to say.

“The Guild Master is deeply disappointed.”

“Th-then?”

“A written report and a pay cut are a given. Prepare yourself for anything beyond that, too.”

“Are you talking about resignation?”

“That depends on the Guild Master.”

“Team Leader, perhaps…”

“Let me tell you up front: don’t ask me for any favors. I don’t have any interest in taking the side of someone who smeared the name of the company I work for. And I have no intention of going against the Guild Master’s wishes.”

“…”

“Whew.”

It was then that Team Leader 1 let out an irritated sigh.

A booming shout echoed from far away.

—Trainee Number One! Im! Chun! Soo!

“……”

“……”

What was that? Were they hearing things?

Team Leader 1 and even the Security Team members, who had all looked ready to die, jumped in surprise. The first to recover his composure was the Security Team Leader.

“Team Leader 1, I’m sorry to bring this up in this kind of atmosphere, but I think I just heard the Guild Master’s voice.”

Team Leader 1, who had been cleaning out his ears, opened his eyes wide.

“Did you hear it too?”

“We heard it, too.”

“But we couldn’t really tell whether it was the Guild Master’s voice… We think we heard a name, though.”

“That was a person’s name? I thought it was just someone screaming.”

“Really? I thought it sounded like someone giving their name and rank.”

Team Leader 1’s face hardened as he listened to the Security Team whispering among themselves.

“Who just said that? What was that about giving a name and rank?”

To him, Im Chunsoo was a respected senior and superior.

Im Chunsoo was an unrivaled Hunter who had been active since the Great Cataclysm and a war hero—and they were saying he had suddenly given his name and rank?

Team Leader 1 had never imagined such a thing. He couldn’t even imagine it.

“Do you still have the leisure to spout this kind of nonsense? Do you think this is something people in their right minds would say?”

“S-sorry.”

“We must have heard it wrong.”

“Everyone, get a hold of yourselves. Understood?”

After issuing his warning, Team Leader 1 started walking again.

That was when it happened.

—No, sirrrrr!

“……”

—I’ll correct it, sirrrr!

“……”

Those were the shouts of a private second class filled with the very essence of his soul.

It took a while before Team Leader 1’s tightly sealed mouth finally opened.

“From now on, we’re running at full speed. Move.”

“M-Move!”

Everyone gathered there was at least a C-rank Hunter. They were superhuman beings who had already far surpassed the limits of ordinary people.

They raced forward like runaway locomotives and reached the entrance to the hiking trail in less than five minutes.

“You’re slow as hell. Took you long enough?”

“Guild Master!”

“Keep your voice down. You’ll burst my eardrums.”

Seeing Im Chunsoo looking the same as always, Team Leader 1 let out a sigh of relief.

“I was worried something might have happened…”

“Something happened? Was there anything strange?”

“N-no, sir. But where did that Jin Taekyung bastard go?”

“I gave him a talking-to and sent him on his way. After speaking with him, I found out he was a better fellow than I expected. Why?”

“I was wondering if he had caused some kind of disturbance.”

“Ah, are you talking about the man shouting earlier?”

“Yes, that’s right. But his voice sounded just like…”

He couldn’t bring himself to finish the sentence.

Just like the Guild Master’s.

Im Chunsoo glared at him.

“Just like what?”

“Oh, it was nothing.”

“What a bland bunch. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?”

“Ah, I see.”

“What was it? I made them do some PT exercises for a while, and they looked ready to die.”

Team Leader 1 felt the suspicions he had been harboring vanish completely.

*I must have been out of my mind. How dare I even think such a thing?*

While he was deeply repenting to himself, Im Chunsoo was tearing into the Security Team.

“Security Team Leader.”

“Y-yes, sir!”

“Oh, you can answer properly. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?”

“I’m sorry, Guild Master!”

“Are the others keeping their mouths shut because they did such a good job? Do I need to make my sword dance today?”

“We’re sorry, Guild Master!”

Team Leader 1 watched the scene with a pleased smile.

Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding senior in life.

*Guild Master. I’ll follow you forever.*

As Team Leader 1 gazed at Im Chunsoo’s back with boundless respect, he suddenly tilted his head.

*…But why is there dirt on the Guild Master’s back?*

He must have scolded those kids rather intensely.

* * *

“We’ve arrived.”

At Butler Kim’s words, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex.

*When did we get here?*

“Th-thank you.”

“Don’t mention it.”

A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an entire era.

*No, this man really did rule an era, too.*

Until now, I had thought of him as nothing more than a senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all.

*He made an A-rank mage—and Im Chunsoo, no less—run around like a dog.*

He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine.

*Trainee, who uses mana during PT exercises?*

*Whack!*

*Trainee Number One Im Chunsoo. S-sorry, sir.*

*Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?*

*No, sirrrrr!*

*Attention. At ease. Attention. At ease.*

*Snap-snap-snap-snap!*

*On your backs. On your fronts. On your backs. On your backs.*

*Gasp.*

*Trainee, didn’t you hear me say on your backs? Get your head straight.*

*I’ll correct it, sirrrr!*

*And why are you bullying an innocent junior? Haven’t I repeatedly emphasized that seniors and juniors should help each other?*

*S-sorry, sir.*

*Repeat after me. Sitting down, cherish your junior; standing up, cherish him. One. Two.*

*Cherish my junior!*

*Trainee, I remember you’re Class 25. Am I right?*

*Trainee Number One Im Chunsoo. Yes, sir.*

*I’m Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.*

*…*

*Why aren’t you answering? Prepare for squat jumps.*

*P-prepare, sir…*

He kept working him over, then working him over some more.

It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day.

*What on earth is Butler Kim’s real identity?*

If someone was Class 3 at the Hunter Training Center, they could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat.

And he had been an instructor, no less.

It would not be an exaggeration to say that every mage from the early days of the Great Cataclysm had passed through his hands.

*His ability as a mage is at least A-rank, too.*

I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill.

There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position.

*But…*

Why was someone that accomplished working as a butler?

I was sneaking a sidelong glance at Butler Kim when our eyes met.

“You seem to have a lot you want to ask.”

“To be honest, I do.”

I was too curious to stand it any longer.

Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth.

“It’s a long story.”

“That’s fine. I’m on vacation, so I have plenty of time.”

“Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.”

“Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.”

“……”
```
